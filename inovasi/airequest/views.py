from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from .models import OpenAIRequest

from .myprompt import get_prompt_analisis_makalah, get_prompt_ideasi
from inovasi.makalah.models import Makalah

import json
import openai
import os


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

            profiling = "Anda adalah software developer senior yang memiliki kepakaran di bidang pembangkitan listrik. Anda sangat paham bagaimana cara kerja pembangkit listrik, proses bisnis terkait, termasuk sisi non teknikal dari perusahaan pembangkit listrik. Bantu saya mengevaluasi karya inovasi. Anda sangat suka memberi masukan yang mencerahkan. Respon Anda tidak menyertakan pembukaan atau penutupan, tidak menambahkan komentar tambahan di akhir. Format harus dalam format html plain text, dengan tags HTML sederhana <ol> <li>[respon]</li> </ol> untuk membuat ordered list."
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
                if makalah_instance.note_pertanyaan is None:
                    makalah_instance.note_pertanyaan = completion_message
                else:
                    makalah_instance.note_pertanyaan += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'kritikan':
                if makalah_instance.note_kritikan is None:
                    makalah_instance.note_kritikan = completion_message
                else:
                    makalah_instance.note_kritikan += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'saran_pengembangan':
                if makalah_instance.note_saran_pengembangan is None:
                    makalah_instance.note_saran_pengembangan = completion_message
                else:
                    makalah_instance.note_saran_pengembangan += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'catatan_kritis_umum':
                if makalah_instance.note_catatan_kritis_umum is None:
                    makalah_instance.note_catatan_kritis_umum = completion_message
                else:
                    makalah_instance.note_catatan_kritis_umum += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'catatan_kritis_aplikasi':
                if makalah_instance.note_catatan_kritis_aplikasi is None:
                    makalah_instance.note_catatan_kritis_aplikasi = completion_message
                else:
                    makalah_instance.note_catatan_kritis_aplikasi += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'ide_manfaat_inovasi':
                if makalah_instance.note_ide_manfaat_inovasi is None:
                    makalah_instance.note_ide_manfaat_inovasi = completion_message
                else:
                    makalah_instance.note_ide_manfaat_inovasi += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'ide_risiko_inovasi':
                if makalah_instance.note_ide_risiko_inovasi is None:
                    makalah_instance.note_ide_risiko_inovasi = completion_message
                else:
                    makalah_instance.note_ide_risiko_inovasi += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'ide_risiko_inovasi_softwarefull':
                if makalah_instance.note_ide_risiko_inovasi_softwarefull is None:
                    makalah_instance.note_ide_risiko_inovasi_softwarefull = completion_message
                else:
                    makalah_instance.note_ide_risiko_inovasi_softwarefull += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'ide_risiko_inovasi_softwarealat':
                if makalah_instance.note_ide_risiko_inovasi_softwarealat is None:
                    makalah_instance.note_ide_risiko_inovasi_softwarealat = completion_message
                else:
                    makalah_instance.note_ide_risiko_inovasi_softwarealat += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'analisis_latar_belakang':
                if makalah_instance.note_analisis_latar_belakang is None:
                    makalah_instance.note_analisis_latar_belakang = completion_message
                else:
                    makalah_instance.note_analisis_latar_belakang += "\n----------\n" + completion_message
            elif inputan_kategori_request == 'analisis_metodologi':
                if makalah_instance.note_analisis_metodologi is None:
                    makalah_instance.note_analisis_metodologi = completion_message
                else:
                    makalah_instance.note_analisis_metodologi += "\n----------\n" + completion_message
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


@csrf_exempt
def openai_request_for_ideasi(request):
    if request.method == 'POST':
        print('POST request received')
        try:
            data = json.loads(request.body)
            inputan_data_ide_judul = data['data_ide_judul']
            inputan_data_latar_belakang = data['data_latar_belakang']
            inputan_data_solusi = data['data_solusi']
            inputan_kategori_request = data['kategori_request']

            profiling = "Anda adalah karyawan senior di perusahaan pembangkitan listrik PLN NP Services. Anda piawai dalam menghasilkan dan memberi kritikan konstruktif terhadap karya inovasi. Bantu saya memberi masukan konstruktif untuk karya inovasi. Anda sangat suka memberi masukan yang mencerahkan. Respon Anda tidak menyertakan pembukaan atau penutupan. Format respon Anda dengan tag html sederhana untuk paragraph <p>[respon]</p> dan untuk membuat ordered list sesuai keperluan <ol> <li>[respon]</li> </ol>"
            narasi_prompt = get_prompt_ideasi(
                inputan_kategori_request, inputan_data_ide_judul, inputan_data_latar_belakang, inputan_data_solusi)

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

         

            return JsonResponse({'generated_idea': completion_message}, status=200)

        except KeyError:
            return JsonResponse({'error': 'Invalid data sent'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except openai.OpenAIError as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error_message': 'Invalid request method'}, status=405)
