import json
import os

translations = {
    'ar': {
        'formSuccessTitle': 'تم إرسال الرسالة!',
        'formSuccessMessage': 'شكرًا لتواصلك معنا. سنرد عليك في أقرب وقت ممكن.',
        'formSendAnother': 'إرسال رسالة أخرى',
        'formErrorMessage': 'حدثت مشكلة أثناء إرسال النموذج. يرجى المحاولة مرة أخرى.'
    },
    'zh': {
        'formSuccessTitle': '消息已发送！',
        'formSuccessMessage': '感谢您的联系。我们将尽快回复您。',
        'formSendAnother': '发送另一条消息',
        'formErrorMessage': '提交表单时出现问题。请重试。'
    },
    'nl': {
        'formSuccessTitle': 'Bericht verzonden!',
        'formSuccessMessage': 'Bedankt voor uw bericht. We nemen zo snel mogelijk contact met u op.',
        'formSendAnother': 'Stuur nog een bericht',
        'formErrorMessage': 'Er is een probleem opgetreden bij het verzenden van uw formulier. Probeer het opnieuw.'
    },
    'en': {
        'formSuccessTitle': 'Message Sent!',
        'formSuccessMessage': 'Thank you for getting in touch. We will get back to you as soon as possible.',
        'formSendAnother': 'Send another message',
        'formErrorMessage': 'There was a problem submitting your form. Please try again.'
    },
    'fr': {
        'formSuccessTitle': 'Message envoyé !',
        'formSuccessMessage': 'Merci de nous avoir contactés. Nous vous répondrons dans les plus brefs délais.',
        'formSendAnother': 'Envoyer un autre message',
        'formErrorMessage': 'Un problème est survenu lors de l\'envoi de votre formulaire. Veuillez réessayer.'
    },
    'de': {
        'formSuccessTitle': 'Nachricht gesendet!',
        'formSuccessMessage': 'Vielen Dank für Ihre Kontaktaufnahme. Wir werden uns so schnell wie möglich bei Ihnen melden.',
        'formSendAnother': 'Eine weitere Nachricht senden',
        'formErrorMessage': 'Beim Senden Ihres Formulars ist ein Problem aufgetreten. Bitte versuchen Sie es erneut.'
    },
    'hi': {
        'formSuccessTitle': 'संदेश भेजा गया!',
        'formSuccessMessage': 'संपर्क करने के लिए धन्यवाद। हम जल्द से जल्द आपसे संपर्क करेंगे।',
        'formSendAnother': 'एक और संदेश भेजें',
        'formErrorMessage': 'आपका फॉर्म सबमिट करने में कोई समस्या थी। कृपया पुनः प्रयास करें।'
    },
    'it': {
        'formSuccessTitle': 'Messaggio inviato!',
        'formSuccessMessage': 'Grazie per averci contattato. Ti risponderemo il prima possibile.',
        'formSendAnother': 'Invia un altro messaggio',
        'formErrorMessage': 'Si è verificato un problema durante l\'invio del modulo. Per favore riprova.'
    },
    'ja': {
        'formSuccessTitle': 'メッセージが送信されました！',
        'formSuccessMessage': 'お問い合わせいただきありがとうございます。できるだけ早くご連絡いたします。',
        'formSendAnother': '別のメッセージを送信する',
        'formErrorMessage': 'フォームの送信中に問題が発生しました。もう一度お試しください。'
    },
    'ko': {
        'formSuccessTitle': '메시지가 전송되었습니다!',
        'formSuccessMessage': '연락해 주셔서 감사합니다. 가능한 한 빨리 답변해 드리겠습니다.',
        'formSendAnother': '다른 메시지 보내기',
        'formErrorMessage': '양식을 제출하는 중에 문제가 발생했습니다. 다시 시도해 주세요.'
    },
    'pt': {
        'formSuccessTitle': 'Mensagem enviada!',
        'formSuccessMessage': 'Obrigado por entrar em contato. Responderemos o mais breve possível.',
        'formSendAnother': 'Enviar outra mensagem',
        'formErrorMessage': 'Ocorreu um problema ao enviar o seu formulário. Por favor, tente novamente.'
    },
    'ru': {
        'formSuccessTitle': 'Сообщение отправлено!',
        'formSuccessMessage': 'Спасибо, что связались с нами. Мы ответим вам как можно скорее.',
        'formSendAnother': 'Отправить еще одно сообщение',
        'formErrorMessage': 'При отправке формы возникла проблема. Пожалуйста, попробуйте еще раз.'
    },
    'es': {
        'formSuccessTitle': '¡Mensaje enviado!',
        'formSuccessMessage': 'Gracias por contactarnos. Nos comunicaremos con usted lo antes posible.',
        'formSendAnother': 'Enviar otro mensaje',
        'formErrorMessage': 'Hubo un problema al enviar su formulario. Por favor, inténtelo de nuevo.'
    },
    'sv': {
        'formSuccessTitle': 'Meddelandet skickat!',
        'formSuccessMessage': 'Tack för att du hörde av dig. Vi återkommer till dig så snart som möjligt.',
        'formSendAnother': 'Skicka ett annat meddelande',
        'formErrorMessage': 'Ett problem uppstod när ditt formulär skickades. Vänligen försök igen.'
    },
    'th': {
        'formSuccessTitle': 'ส่งข้อความแล้ว!',
        'formSuccessMessage': 'ขอบคุณที่ติดต่อเรา เราจะติดต่อกลับโดยเร็วที่สุด',
        'formSendAnother': 'ส่งข้อความอื่น',
        'formErrorMessage': 'เกิดปัญหาในการส่งแบบฟอร์มของคุณ กรุณาลองอีกครั้ง'
    }
}

base_dir = '/Users/tlotlisomofokeng/Documents/GitHub/travelhawkdev.github.io/translations'
for lang, trans in translations.items():
    file_path = os.path.join(base_dir, f"{lang}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        data.update(trans)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')
