from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from .models import OpenAIRequest

from .myprompt import get_prompt_analisis_makalah
from inovasi.makalah.models import Makalah

import json
import openai
import os
import re


@csrf_exempt
def openai_request(request):
    if request.method == 'POST':
        print('POST request received')    
        try:
            data = json.loads(request.body)
            id_makalah = data['data_id_makalah']
            inputan_judul_makalah = data['data_judul_makalah']
            inputan_abstrak = data['data_abstrak']
            inputan_klaim = data['data_klaim']
            inputan_latar_belakang = data['data_latar_belakang']
            inputan_maksud_tujuan = data['data_maksud_tujuan']
            inputan_identifikasi_masalah = data['data_identifikasi_masalah']
            inputan_analisis_masalah = data['data_analisis_masalah']
            inputan_metodologi = data['data_metodologi']
            inputan_desain_inovasi = data['data_desain_inovasi']
            inputan_implementasi = data['data_implementasi']
            inputan_evaluasi_implementasi = data['data_evaluasi_implementasi']
            inputan_manfaat_finansial = data['data_manfaat_finansial']
            inputan_manfaat_non_finansial = data['data_manfaat_non_finansial']
            inputan_daftar_pustaka = data['data_daftar_pustaka']
            inputan_kategori_request = data['kategori_request']

            profiling = "Anda adalah software developer senior yang memiliki kepakaran di bidang pembangkitan listrik. Anda sangat paham bagaimana cara kerja pembangkit listrik, proses bisnis terkait, termasuk sisi non teknikal dari perusahaan pembangkit listrik. Bantu saya mengevaluasi karya inovasi di bidang pembuatan perangkat lunak. Anda sangat suka memberi masukan yang mencerahkan. Berikan respons dalam bentuk daftar berformat markdown, tidak menyertakan pembukaan atau penutupan, tidak menambahkan komentar tambahan di akhir. Format harus dalam format html plain text, dengan tags HTML sederhana untuk membuat ordered list. Gunakan cetak tebal dan italic untuk memberi penekanan, hanya jika diperlukan."
            narasi_prompt = get_prompt_analisis_makalah(
                inputan_kategori_request, inputan_judul_makalah, inputan_abstrak, inputan_klaim, inputan_latar_belakang, inputan_maksud_tujuan, inputan_identifikasi_masalah, inputan_analisis_masalah, inputan_metodologi, inputan_desain_inovasi, inputan_implementasi, inputan_evaluasi_implementasi, inputan_manfaat_finansial, inputan_manfaat_non_finansial, inputan_daftar_pustaka)

            client = OpenAI(
                api_key=os.environ['OPENAI_API_KEY'],
            )
            completion = client.chat.completions.create(
                # model="gpt-3.5-turbo",
                model="gpt-4-0613",
                messages=[
                    {"role": "system", "content": profiling},
                    {"role": "user", "content": narasi_prompt}
                ]
            )

            completion_message = completion.choices[0].message.content

            # Create an instance of OpenAIRequest and save it to the database
            openai_request = OpenAIRequest(
                pembuat_request=request.user,
                pembuat_username=request.user.username,
                kategori_umum=inputan_kategori_request,
                input_request=narasi_prompt,
                output_request=completion_message,
                prompt_tokens=completion.usage.prompt_tokens,
                completion_tokens=completion.usage.completion_tokens,
                total_tokens=completion.usage.total_tokens,
                input_words_count=len(narasi_prompt.split()),
                output_words_count=len(completion_message.split())
            )
            openai_request.save()

            makalah_instance = Makalah.objects.get(pk=id_makalah)
            if inputan_kategori_request == 'pertanyaan':

                # # Remove numbers at the start of each item
                # completion_message = re.sub(r'\d+\.\s', '', completion_message)

                # # Split items based on '? '
                # completion_message_items = completion_message.split('? ')

                # # Add back the question mark at the end of each item, except for the last one
                # completion_message_items = [f'{item}?' for item in completion_message_items[:-1]] + [completion_message_items[-1]]

                # # Format as an HTML list
                # completion_message_items = [f'<li>{item}</li>' for item in completion_message_items if item]
                # completion_message_html = f'<ul>{" ".join(completion_message_items)}</ul>'

                if makalah_instance.note_pertanyaan is None:
                    makalah_instance.note_pertanyaan = completion_message
                else:
                    makalah_instance.note_pertanyaan += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'ide_manfaat_inovasi':
                makalah_instance.note_manfaat_inovasi = completion_message

            makalah_instance.save()

            return JsonResponse({'generated_idea': completion_message}, status=200)

        except KeyError:
            return JsonResponse({'error': 'Invalid data sent'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except openai.OpenAIError as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error_message': 'Invalid request method'}, status=405)
