import json
import os

translations = {
    'ar': {
        'showcase3Title': 'مناطق أمان محلية للغاية',
        'showcase3Text': 'حدد مناطق الخطر الدقيقة باستخدام خرائط خطورة مرمزة بالألوان وعلامات محددة لحوادث الاختطاف والسرقة في منطقتك المباشرة.',
        'showcase4Title': 'رؤى سلامة الوجهة',
        'showcase4Text': 'استكشف مناطق الجذب الشهيرة في جنوب إفريقيا مثل Franschhoek Wine Tram. راجع معلومات السلامة المدعومة بخرائط الحرارة في الوقت الفعلي لاتخاذ قرارات مستنيرة قبل زيارتك.'
    },
    'de': {
        'showcase3Title': 'Hyperlokale Sicherheitszonen',
        'showcase3Text': 'Identifizieren Sie genaue Gefahrenzonen mit farbcodierten Schweregradkarten und gezielten spezifischen Markierungen für Entführungen und Blitzeinbrüche in Ihrer unmittelbaren Umgebung.',
        'showcase4Title': 'Einblicke in die Sicherheit von Reisezielen',
        'showcase4Text': 'Entdecken Sie beliebte südafrikanische Sehenswürdigkeiten wie die Franschhoek Wine Tram. Überprüfen Sie Sicherheitsinformationen, die durch unsere Echtzeit-Heatmaps unterstützt werden, um fundierte Entscheidungen vor Ihrem Besuch zu treffen.'
    },
    'es': {
        'showcase3Title': 'Zonas de seguridad hiperlocales',
        'showcase3Text': 'Identifique zonas de peligro exactas con mapas de gravedad codificados por colores y marcadores específicos localizados para secuestros y robos violentos en su área inmediata.',
        'showcase4Title': 'Información de seguridad del destino',
        'showcase4Text': 'Explore atracciones populares de Sudáfrica como el Franschhoek Wine Tram. Revise la información de seguridad basada en nuestros mapas de calor en tiempo real para tomar decisiones informadas antes de su visita.'
    },
    'fr': {
        'showcase3Title': 'Zones de sécurité hyper-locales',
        'showcase3Text': 'Identifiez les zones de danger exactes avec des cartes de gravité codées par couleur et des marqueurs spécifiques localisés pour les détournements et les vols à la portière dans votre région immédiate.',
        'showcase4Title': 'Informations sur la sécurité des destinations',
        'showcase4Text': 'Explorez des attractions sud-africaines populaires comme le Franschhoek Wine Tram. Consultez les informations de sécurité basées sur nos cartes thermiques en temps réel pour prendre des décisions éclairées avant votre visite.'
    },
    'hi': {
        'showcase3Title': 'हाइपर-लोकल सुरक्षा क्षेत्र',
        'showcase3Text': 'रंग-कोडित गंभीरता मानचित्रों के साथ सटीक खतरे वाले क्षेत्रों की पहचान करें और अपने तत्काल क्षेत्र में अपहरण और लूटपाट के लिए विशिष्ट मार्करों को इंगित करें।',
        'showcase4Title': 'गंतव्य सुरक्षा जानकारी',
        'showcase4Text': 'फ्रैंशहोक वाइन ट्राम जैसे लोकप्रिय दक्षिण अफ्रीकी आकर्षणों का अन्वेषण करें। अपनी यात्रा से पहले सोच-समझकर निर्णय लेने के लिए हमारे रीयल-टाइम हीटमैप द्वारा संचालित सुरक्षा जानकारी की समीक्षा करें।'
    },
    'it': {
        'showcase3Title': 'Zone di sicurezza iperlocali',
        'showcase3Text': 'Identifica le zone di pericolo esatte con mappe di gravità codificate a colori e marcatori specifici localizzati per dirottamenti e furti con scasso nelle tue immediate vicinanze.',
        'showcase4Title': 'Approfondimenti sulla sicurezza delle destinazioni',
        'showcase4Text': 'Esplora le famose attrazioni sudafricane come il Franschhoek Wine Tram. Consulta le informazioni sulla sicurezza basate sulle nostre mappe termiche in tempo reale per prendere decisioni informate prima della tua visita.'
    },
    'ja': {
        'showcase3Title': 'ハイパーローカル安全ゾーン',
        'showcase3Text': '色分けされた重大度マップを使用して正確な危険ゾーンを特定し、すぐ近くの地域でのハイジャックやひったくりなどの特定のマーカーをピンポイントで示します。',
        'showcase4Title': '目的地の安全に関する洞察',
        'showcase4Text': 'フランシュフック・ワイン・トラムなど、南アフリカの人気の観光スポットを探索しましょう。リアルタイムのヒートマップを活用した安全情報を確認し、訪問前に情報に基づいた決定を下すことができます。'
    },
    'ko': {
        'showcase3Title': '초국지적 안전 구역',
        'showcase3Text': '색상으로 구분된 심각도 지도를 사용하여 정확한 위험 구역을 식별하고, 인근 지역의 납치 및 차량 털이에 대한 특정 마커를 찾아냅니다.',
        'showcase4Title': '목적지 안전 정보',
        'showcase4Text': '프란슈훅 와인 트램과 같은 인기 있는 남아프리카 명소를 탐험하세요. 실시간 히트맵 기반의 안전 정보를 검토하여 방문하기 전에 정보에 입각한 결정을 내리세요.'
    },
    'nl': {
        'showcase3Title': 'Hyperlokale veiligheidszones',
        'showcase3Text': 'Identificeer exacte gevarenzones met kleurgecodeerde ernstkaarten en gerichte specifieke markeringen voor kapingen en smash-and-grabs in uw directe omgeving.',
        'showcase4Title': 'Inzichten in bestemmingsveiligheid',
        'showcase4Text': 'Verken populaire Zuid-Afrikaanse attracties zoals de Franschhoek Wine Tram. Bekijk veiligheidsinformatie op basis van onze realtime heatmaps om weloverwogen beslissingen te nemen voordat u op bezoek gaat.'
    },
    'pt': {
        'showcase3Title': 'Zonas de segurança hiperlocais',
        'showcase3Text': 'Identifique zonas de perigo exatas com mapas de gravidade codificados por cores e marcadores específicos localizados para sequestros e roubos em sua área imediata.',
        'showcase4Title': 'Informações de segurança do destino',
        'showcase4Text': 'Explore atrações populares da África do Sul, como o Franschhoek Wine Tram. Revise as informações de segurança fornecidas por nossos mapas de calor em tempo real para tomar decisões informadas antes de sua visita.'
    },
    'ru': {
        'showcase3Title': 'Гиперлокальные зоны безопасности',
        'showcase3Text': 'Определяйте точные зоны опасности с помощью тепловых карт с цветовой кодировкой и конкретных маркеров угонов и краж со взломом в вашем непосредственном окружении.',
        'showcase4Title': 'Информация о безопасности пункта назначения',
        'showcase4Text': 'Исследуйте популярные достопримечательности Южной Африки, такие как винный трамвай Франшхука. Ознакомьтесь с информацией о безопасности на основе наших тепловых карт в реальном времени, чтобы принимать обоснованные решения перед визитом.'
    },
    'sv': {
        'showcase3Title': 'Hyperlokala säkerhetszoner',
        'showcase3Text': 'Identifiera exakta farozoner med färgkodade allvarlighetskartor och specifika markörer för kapningar och inbrott i ditt omedelbara närområde.',
        'showcase4Title': 'Insikter om resmålets säkerhet',
        'showcase4Text': 'Utforska populära sydafrikanska sevärdheter som Franschhoek Wine Tram. Granska säkerhetsinformation som drivs av våra värmekartor i realtid för att fatta välgrundade beslut före ditt besök.'
    },
    'th': {
        'showcase3Title': 'โซนความปลอดภัยแบบไฮเปอร์โลคอล',
        'showcase3Text': 'ระบุโซนอันตรายที่แน่นอนด้วยแผนที่ความรุนแรงที่ใช้รหัสสี และระบุเครื่องหมายเฉพาะสำหรับการปล้นจี้และทุบกระจกขโมยของในพื้นที่ใกล้เคียงของคุณ',
        'showcase4Title': 'ข้อมูลความปลอดภัยของจุดหมายปลายทาง',
        'showcase4Text': 'สำรวจสถานที่ท่องเที่ยวยอดนิยมในแอฟริกาใต้ เช่น Franschhoek Wine Tram ตรวจสอบข้อมูลความปลอดภัยที่ขับเคลื่อนโดยแผนที่ความร้อนแบบเรียลไทม์ของเราเพื่อประกอบการตัดสินใจก่อนการเดินทางของคุณ'
    },
    'zh': {
        'showcase3Title': '超本地安全区',
        'showcase3Text': '使用彩色编码的严重程度地图识别确切的危险区域，并精确定位您附近区域的劫车和砸窗抢劫的具体标记。',
        'showcase4Title': '目的地安全洞察',
        'showcase4Text': '探索弗朗斯胡克葡萄酒电车等南非热门景点。在访问之前，查看由我们的实时热图提供支持的安全信息，以做出明智的决定。'
    }
}

base_dir = '/Users/tlotlisomofokeng/Documents/GitHub/travelhawkdev.github.io/translations'
for lang, trans in translations.items():
    file_path = os.path.join(base_dir, f"{lang}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        data['showcase3Title'] = trans['showcase3Title']
        data['showcase3Text'] = trans['showcase3Text']
        data['showcase4Title'] = trans['showcase4Title']
        data['showcase4Text'] = trans['showcase4Text']
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')
