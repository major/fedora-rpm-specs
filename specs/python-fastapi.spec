# This package corresponds to two PyPI projects (fastapi-slim, and fastapi)
# co-developed in one repository. Since the two are versioned identically and
# released at the same time, it makes sense to build them from a single source
# package. (The fastapi-cli package is versioned and packaged separately.)

# Breaks a circular dependency on fastapi-cli by omitting it from fastapi’s
# “standard”, “standard-no-fastapi-cloud-cli”, and “all” extras.
%bcond bootstrap 0

%bcond inline_snapshot 1
%bcond orjson 1
%bcond passlib 1
# Not yet packaged: https://pypi.org/project/PyJWT/
%bcond pyjwt 0
# Python 3.14 / Pydantic 3.12 / PEP 649 compat. issues; orphaned for F43
%bcond sqlmodel %[ %{without bootstrap} && 0 ]
%bcond uvicorn 1

# For translations, check docs/*/docs/index.md
# Note that there are many other localized versions of the documentation
# *present*, but untranslated.
%global sum_de FastAPI-Framework
%global sum_en FastAPI framework
# Upstream has an “em” (emoji) translation, but we consider this a joke rather
# than a proper translation: “em” is not an assigned ISO 639-1 code.
%global sum_es FastAPI framework
%global sum_fa فریم‌ورک FastAPI
%global sum_fr Framework FastAPI
%global sum_ja FastAPI framework
%global sum_ko FastAPI 프레임워크
%global sum_pt Framework FastAPI
%global sum_ru Фреймворк FastAPI
%global sum_tr FastAPI framework
%global sum_uk Готовий до продакшину
%global sum_vi FastAPI framework
%global sum_zh_hant FastAPI 框架
%global sum_zh FastAPI 框架

Name:           python-fastapi
Version:        0.120.1
Release:        %autorelease
Summary:        %{sum_en}

# SPDX
License:        MIT
URL:            https://github.com/fastapi/fastapi
Source:         %{url}/archive/%{version}/fastapi-%{version}.tar.gz

# Written for Fedora in groff_man(7) format based on --help output
Source10:       fastapi.1
Source11:       fastapi-dev.1
Source12:       fastapi-run.1
Source13:       fastapi-deploy.1
Source14:       fastapi-login.1
Source15:       fastapi-logout.1

BuildArch:      noarch

# Downstream-only: run test_fastapi_cli without coverage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-run-test_fastapi_cli-without-coverag.patch

BuildRequires:  python3-devel

# Since requirements-tests.txt and requirements-docs-tests.txt contain
# overly-strict version bounds and many unwanted
# linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the test dependencies we *do* want manually rather than trying
# to patch the requirements files. We preserve upstream’s lower bounds but
# remove upper bounds, as we must try to make do with what we have.
#
# requirements-docs-tests.txt:
# # For mkdocstrings and tests
BuildRequires:  %{py3_dist httpx} >= 0.23
# requirements-tests.txt:
BuildRequires:  %{py3_dist pytest} >= 7.1.3
BuildRequires:  %{py3_dist dirty-equals} >= 0.9
%if %{with sqlmodel}
BuildRequires:  %{py3_dist sqlmodel} >= 0.0.24
%endif
BuildRequires:  %{py3_dist flask} >= 1.1.2
BuildRequires:  %{py3_dist anyio[trio]} >= 3.2.1
# Omit PyJWT, https://pypi.org/project/PyJWT/, because it is not packaged and
# only has very limited use in the tests.
%if %{with pyjwt}
BuildRequires:  %{py3_dist PyJWT} >= 2.9
%endif
BuildRequires:  %{py3_dist pyyaml} >= 5.3.1
%if %{with passlib}
BuildRequires:  %{py3_dist passlib[bcrypt]} >= 1.7.2
%endif
%if %{with inline_snapshot}
BuildRequires:  %{py3_dist inline-snapshot} >= 0.21.1
%endif
# This is still needed in the tests even if we do not have sqlmodel to bring it
# in as an indirect dependency.
BuildRequires:  %{py3_dist sqlalchemy}

Summary(de):    %{sum_de}
Summary(en):    %{sum_en}
Summary(es):    %{sum_es}
Summary(fa):    %{sum_fa}
Summary(fr):    %{sum_fr}
Summary(ja):    %{sum_ja}
Summary(ko):    %{sum_ko}
Summary(pt):    %{sum_pt}
Summary(ru):    %{sum_ru}
Summary(tr):    %{sum_tr}
Summary(uk):    %{sum_uk}
Summary(vi):    %{sum_vi}
Summary(zh-Hant):    %{sum_zh_hant}
Summary(zh):    %{sum_zh}

%global common_description_de %{expand:
FastAPI ist ein modernes, schnelles (hoch performantes) Webframework zur
Erstellung von APIs mit Python auf Basis von Standard-Python-Typhinweisen.

Seine Schlüssel-Merkmale sind:

  • Schnell: Sehr hohe Performanz, auf Augenhöhe mit NodeJS und Go (dank
    Starlette und Pydantic). Eines der schnellsten verfügbaren
    Python-Frameworks.
  • Schnell zu entwickeln: Erhöhen Sie die Geschwindigkeit bei der Entwicklung
    von Features um etwa 200 % bis 300 %. *
  • Weniger Bugs: Verringern Sie die von Menschen (Entwicklern) verursachten
    Fehler um etwa 40 %. *
  • Intuitiv: Hervorragende Editor-Unterstützung. Code-Vervollständigung
    überall. Weniger Zeit mit Debuggen verbringen.
  • Einfach: So konzipiert, dass es einfach zu benutzen und zu erlernen ist.
    Weniger Zeit mit dem Lesen von Dokumentation verbringen.
  • Kurz: Minimieren Sie die Verdoppelung von Code. Mehrere Features aus jeder
    Parameterdeklaration. Weniger Bugs.
  • Robust: Erhalten Sie produktionsreifen Code. Mit automatischer,
    interaktiver Dokumentation.
  • Standards-basiert: Basierend auf (und vollständig kompatibel mit) den
    offenen Standards für APIs: OpenAPI (früher bekannt als Swagger) und JSON
    Schema.

* Schätzung basierend auf Tests in einem internen Entwicklungsteam, das
Produktionsanwendungen erstellt.}

%global common_description_en %{expand:
FastAPI is a modern, fast (high-performance), web framework for building APIs
with Python based on standard Python type hints.

The key features are:

  • Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette
    and Pydantic). One of the fastest Python frameworks available.
  • Fast to code: Increase the speed to develop features by about 200% to
    300%. *
  • Fewer bugs: Reduce about 40% of human (developer) induced errors. *
  • Intuitive: Great editor support. Completion everywhere. Less time
    debugging.
  • Easy: Designed to be easy to use and learn. Less time reading docs.
  • Short: Minimize code duplication. Multiple features from each parameter
    declaration. Fewer bugs.
  • Robust: Get production-ready code. With automatic interactive
    documentation.
  • Standards-based: Based on (and fully compatible with) the open standards
    for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

* estimation based on tests on an internal development team, building
  production applications.}

%global common_description_es %{expand:
FastAPI es un framework web moderno, rápido (de alto rendimiento), para
construir APIs con Python basado en las anotaciones de tipos estándar de
Python.

Las características clave son:

  • Rápido: Muy alto rendimiento, a la par con NodeJS y Go (gracias a Starlette
    y Pydantic). Uno de los frameworks Python más rápidos disponibles.
  • Rápido de programar: Aumenta la velocidad para desarrollar funcionalidades
    en aproximadamente un 200% a 300%. *
  • Menos bugs: Reduce en aproximadamente un 40% los errores inducidos por
    humanos (desarrolladores). *
  • Intuitivo: Gran soporte para editores. Autocompletado en todas partes.
    Menos tiempo depurando.
  • Fácil: Diseñado para ser fácil de usar y aprender. Menos tiempo leyendo
    documentación.
  • Corto: Minimiza la duplicación de código. Múltiples funcionalidades desde
    cada declaración de parámetro. Menos bugs.
  • Robusto: Obtén código listo para producción. Con documentación interactiva
    automática.
  • Basado en estándares: Basado (y completamente compatible) con los
    estándares abiertos para APIs: OpenAPI (anteriormente conocido como
    Swagger) y JSON Schema.

* estimación basada en pruebas con un equipo de desarrollo interno,
construyendo aplicaciones de producción.}

%global common_description_fa %{expand:
FastAPI یک وب فریم‌ورک مدرن و سریع (با کارایی بالا) برای ایجاد APIهای متنوع
(وب، وب‌سوکت و غبره) با زبان پایتون نسخه +۳.۶ است. این فریم‌ورک با
رعایت کامل راهنمای نوع داده (Type Hint) ایجاد شده است.

ویژگی‌های کلیدی این فریم‌ورک عبارتند از:

  • سرعت: کارایی بسیار بالا و قابل مقایسه با NodeJS و Go (با تشکر از Starlette و
    Pydantic). یکی از سریع‌ترین فریم‌ورک‌های پایتونی موجود.

  • کدنویسی سریع: افزایش ۲۰۰ تا ۳۰۰ درصدی سرعت توسعه قابلیت‌های جدید. *

  • باگ کمتر: کاهش ۴۰ درصدی خطاهای انسانی (برنامه‌نویسی). *

  • هوشمندانه: پشتیبانی فوق‌العاده در محیط‌های توسعه یکپارچه (IDE).
    تکمیل در همه بخش‌های کد. کاهش زمان رفع باگ.

  • آسان: طراحی شده برای یادگیری و استفاده آسان. کاهش زمان مورد نیاز برای
    مراجعه به مستندات.

  • کوچک: کاهش تکرار در کد. چندین قابلیت برای هر پارامتر (منظور پارامترهای
    ورودی تابع هندلر می‌باشد، به بخش خلاصه در همین صفحه مراجعه شود). باگ
    کمتر.

  • استوار: ایجاد کدی آماده برای استفاده در محیط پروداکشن و تولید خودکار
    مستندات تعاملی

  • مبتنی بر استانداردها: مبتنی بر (و منطبق با) استانداردهای متن باز مربوط به
    API: OpenAPI (سوگر سابق) و JSON Schema.

* تخمین‌ها بر اساس تست‌های انجام شده در یک تیم توسعه داخلی که مشغول
  ایجاد برنامه‌های کاربردی واقعی بودند صورت گرفته است.}

%global common_description_fr %{expand:
FastAPI est un framework web moderne et rapide (haute performance) pour la
création d'API avec Python, basé sur les annotations de type standard de
Python.

Les principales fonctionnalités sont :

  • Rapidité : De très hautes performances, au niveau de NodeJS et Go (grâce à
    Starlette et Pydantic). L'un des frameworks Python les plus rapides.
  • Rapide à coder : Augmente la vitesse de développement des fonctionnalités
    d'environ 200 % à 300 %. *
  • Moins de bugs : Réduit d'environ 40 % les erreurs induites par le
    développeur. *
  • Intuitif : Excellente compatibilité avec les IDE. Complétion complète.
    Moins de temps passé à déboguer.
  • Facile : Conçu pour être facile à utiliser et à apprendre. Moins de temps
    passé à lire la documentation.
  • Concis : Diminue la duplication de code. De nombreuses fonctionnalités
    liées à la déclaration de chaque paramètre. Moins de bugs.
  • Robuste : Obtenez un code prêt pour la production. Avec une documentation
    interactive automatique.
  • Basé sur des normes : Basé sur (et entièrement compatible avec) les
    standards ouverts pour les APIs : OpenAPI (précédemment connu sous le nom
de Swagger) et JSON Schema.

* estimation basée sur des tests d'une équipe de développement interne,
construisant des applications de production.}

%global common_description_ja %{expand:
FastAPI は、Pythonの標準である型ヒントに基づいてPython 以降でAPI
を構築するための、モダンで、高速(高パフォーマンス)な、Web フレームワークです。

主な特徴:

  • 高速: NodeJS や Go 並みのとても高いパフォーマンス (Starlette と Pydantic
    のおかげです)。 最も高速な Python フレームワークの一つです.

  • 高速なコーディング: 開発速度を約 200%~300%向上させます。 *

  • 少ないバグ: 開発者起因のヒューマンエラーを約 40％削減します。 *

  • 直感的: 素晴らしいエディタのサポートや オートコンプリート。
    デバッグ時間を削減します。

  • 簡単: 簡単に利用、習得できるようにデザインされています。
    ドキュメントを読む時間を削減します。

  • 短い: コードの重複を最小限にしています。
    各パラメータからの複数の機能。少ないバグ。

  • 堅牢性: 自動対話ドキュメントを使用して、
    本番環境で使用できるコードを取得します。

  • Standards-based: API のオープンスタンダードに基づいており、
    完全に互換性があります: OpenAPI (以前は Swagger として知られていました)
    や JSON スキーマ.

* 本番アプリケーションを構築している開発チームのテストによる見積もり。}

%global common_description_ko %{expand:
FastAPI는 현대적이고, 빠르며(고성능), 파이썬 표준 타입 힌트에 기초한 Python의
API를 빌드하기 위한 웹 프레임워크입니다.

주요 특징으로:

  • 빠름: (Starlette과 Pydantic 덕분에) NodeJS 및 Go와 대등할 정도로 매우 높은
    성능. 사용 가능한 가장 빠른 파이썬 프레임워크 중 하나.

  • 빠른 코드 작성: 약 200%에서 300%까지 기능 개발 속도 증가. *

  • 적은 버그: 사람(개발자)에 의한 에러 약 40% 감소. *

  • 직관적: 훌륭한 편집기 지원. 모든 곳에서 자동완성. 적은 디버깅 시간.

  • 쉬움: 쉽게 사용하고 배우도록 설계. 적은 문서 읽기 시간.

  • 짧음: 코드 중복 최소화. 각 매개변수 선언의 여러 기능. 적은 버그.

  • 견고함: 준비된 프로덕션 용 코드를 얻으십시오. 자동 대화형 문서와 함께.

  • 표준 기반: API에 대한 (완전히 호환되는) 개방형 표준 기반: OpenAPI (이전에
    Swagger로 알려졌던) 및 JSON 스키마.

* 내부 개발팀의 프로덕션 애플리케이션을 빌드한 테스트에 근거한 측정}

%global common_description_pt %{expand:
FastAPI é um moderno e rápido (alta performance) framework web para construção
de APIs com Python, baseado nos type hints padrões do Python.

Os recursos chave são:

  • Rápido: alta performance, equivalente a NodeJS e Go (graças ao Starlette e
    Pydantic). Um dos frameworks mais rápidos disponíveis.
  • Rápido para codar: Aumenta a velocidade para desenvolver recursos entre
    200% a 300%. *
  • Poucos bugs: Reduz cerca de 40% de erros induzidos por humanos
    (desenvolvedores). *
  • Intuitivo: Grande suporte a IDEs. Auto-Complete em todos os lugares. Menos
    tempo debugando.
  • Fácil: Projetado para ser fácil de aprender e usar. Menos tempo lendo
    documentação.
  • Enxuto: Minimize duplicação de código. Múltiplos recursos para cada
    declaração de parâmetro. Menos bugs.
  • Robusto: Tenha código pronto para produção. E com documentação interativa
    automática.
  • Baseado em padrões: Baseado em (e totalmente compatível com) os padrões
    abertos para APIs: OpenAPI (anteriormente conhecido como Swagger) e JSON
    Schema.

* estimativas baseadas em testes realizados com equipe interna de
desenvolvimento, construindo aplicações em produção.}

%global common_description_ru %{expand:
FastAPI — это современный, быстрый (высокопроизводительный) веб-фреймворк для
создания API на Python, основанный на стандартных аннотациях типов Python.

Ключевые особенности:

  • Скорость: Очень высокая производительность, на уровне NodeJS и Go
    (благодаря Starlette и Pydantic). Один из самых быстрых доступных
    фреймворков Python.
  • Быстрота разработки: Увеличьте скорость разработки фич примерно на
    200–300%. *
  • Меньше ошибок: Сократите примерно на 40% количество ошибок, вызванных
    человеком (разработчиком). *
  • Интуитивность: Отличная поддержка редактора кода. Автозавершение везде.
    Меньше времени на отладку.
  • Простота: Разработан так, чтобы его было легко использовать и осваивать.
    Меньше времени на чтение документации.
  • Краткость: Минимизируйте дублирование кода. Несколько возможностей из
    каждого объявления параметров. Меньше ошибок.
  • Надежность: Получите код, готовый к продакшн. С автоматической
    интерактивной документацией.
  • На основе стандартов: Основан на открытых стандартах API и полностью
    совместим с ними: OpenAPI (ранее известный как Swagger) и JSON Schema.

* оценка на основе тестов внутренней команды разработчиков, создающих
продакшн-приложения.}

%global common_description_tr %{expand:
FastAPI, Python 'nin standart tip belirteçlerine dayalı, modern ve hızlı
(yüksek performanslı) API'lar oluşturmak için kullanılabilecek web
framework'tür.

Temel özellikleri şunlardır:

  • Hızlı: Çok yüksek performanslı, NodeJS ve Go ile eşit düzeyde (Starlette ve
    Pydantic sayesinde). En hızlı Python framework'lerinden bir tanesidir.
  • Kodlaması Hızlı: Geliştirme hızını yaklaşık %200 ile %300 aralığında
    arttırır. *
  • Daha az hata: İnsan (geliştirici) kaynaklı hataları yaklaşık %40 azaltır. *
  • Sezgisel: Muhteşem bir editör desteği. Her yerde otomatik tamamlama. Hata
    ayıklama ile daha az zaman harcayacaksınız.
  • Kolay: Öğrenmesi ve kullanması kolay olacak şekilde tasarlandı. Doküman
    okuma ile daha az zaman harcayacaksınız.
  • Kısa: Kod tekrarı minimize edildi. Her parametre tanımlamasında birden
    fazla özellik ve daha az hatayla karşılaşacaksınız.
  • Güçlü: Otomatik ve etkileşimli dokümantasyon ile birlikte, kullanıma hazır
    kod elde edebilirsiniz.
  • Standard öncelikli: API'lar için açık standartlara dayalı (ve tamamen
    uyumlu); OpenAPI (eski adıyla Swagger) ve JSON Schema.

* ilgili kanılar, dahili geliştirme ekibinin geliştirdikleri ürünlere
yaptıkları testlere dayanmaktadır.}

%global common_description_uk %{expand:
FastAPI - це сучасний, швидкий (високопродуктивний), вебфреймворк для створення
API за допомогою Python,в основі якого лежить стандартна анотація типів Python.

Ключові особливості:

  • Швидкий: Дуже висока продуктивність, на рівні з NodeJS та Go (завдяки
    Starlette та Pydantic). Один із найшвидших фреймворків.

  • Швидке написання коду: Пришвидшує розробку функціоналу приблизно на
    200%-300%. *

  • Менше помилок: Зменшить кількість помилок спричинених людиною (розробником)
    на 40%. *

  • Інтуїтивний: Чудова підтримка редакторами коду. Доповнення всюди. Зменште
    час на налагодження.

  • Простий: Спроектований, для легкого використання та навчання. Знадобиться
    менше часу на читання документації.

  • Короткий: Зведе до мінімуму дублювання коду. Кожен оголошений параметр може
    виконувати кілька функцій.

  • Надійний: Ви матимете стабільний код готовий до продакшину з автоматичною
    інтерактивною документацією.

  • Стандартизований: Оснований та повністю сумісний з відкритими стандартами
    для API: OpenAPI (попередньо відомий як Swagger) та JSON Schema.

* оцінка на основі тестів внутрішньої команди розробників, створення
продуктових застосунків.}

%global common_description_vi %{expand:
FastAPI là một web framework hiện đại, hiệu năng cao để xây dựng web APIs với
Python dựa trên tiêu chuẩn Python type hints.

Những tính năng như:

  • Nhanh: Hiệu năng rất cao khi so sánh với NodeJS và Go (cảm ơn Starlette và
    Pydantic). Một trong những Python framework nhanh nhất.
  • Code nhanh: Tăng tốc độ phát triển tính năng từ 200% tới 300%. *
  • Ít lỗi hơn: Giảm khoảng 40% những lỗi phát sinh bởi con người (nhà phát
    triển). *
  • Trực giác tốt hơn: Được các trình soạn thảo hỗ tuyệt vời. Completion mọi
    nơi. Ít thời gian gỡ lỗi.
  • Dễ dàng: Được thiết kế để dễ dàng học và sử dụng. Ít thời gian đọc tài
    liệu.
  • Ngắn: Tối thiểu code bị trùng lặp. Nhiều tính năng được tích hợp khi định
    nghĩa tham số. Ít lỗi hơn.
  • Tăng tốc: Có được sản phẩm cùng với tài liệu (được tự động tạo) có thể
    tương tác.
  • Được dựa trên các tiêu chuẩn: Dựa trên (và hoàn toàn tương thích với) các
    tiêu chuẩn mở cho APIs : OpenAPI (trước đó được biết đến là Swagger) và
    JSON Schema.

* ước tính được dựa trên những kiểm chứng trong nhóm phát triển nội bộ, xây
dựng các ứng dụng sản phẩm.}

%global common_description_zh_hant %{expand:
FastAPI 是一個現代、快速（高效能）的 web 框架，用於 Python 並採用標準 Python
型別提示。

主要特點包含：

  • 快速： 非常高的效能，可與 NodeJS 和 Go 效能相當 (歸功於 Starlette and
    Pydantic)。 FastAPI 是最快的 Python web 框架之一。
  • 極速開發： 提高開發功能的速度約 200% 至 300%。 *
  • 更少的 Bug： 減少約 40% 的人為（開發者）導致的錯誤。 *
  • 直覺： 具有出色的編輯器支援，處處都有自動補全以減少偵錯時間。
  • 簡單： 設計上易於使用和學習，大幅減少閱讀文件的時間。
  • 簡潔： 最小化程式碼重複性。可以通過不同的參數聲明來實現更豐富的功能，
    和更少的錯誤。
  • 穩健： 立即獲得生產級可用的程式碼，還有自動生成互動式文件。
  • 標準化： 基於 (且完全相容於) OpenAPIs 的相關標準：OpenAPI（之前被稱為
    Swagger）和JSON Schema。

* 基於內部開發團隊在建立生產應用程式時的測試預估。}

%global common_description_zh %{expand:
FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python
并基于标准的 Python 类型提示。

关键特性:

  • 快速：可与 NodeJS 和 Go 并肩的极高性能（归功于 Starlette 和
    Pydantic）。最快的 Python web 框架之一。
  • 高效编码：提高功能开发速度约 200％ 至 300％。*
  • 更少 bug：减少约 40％ 的人为（开发者）导致错误。*
  • 智能：极佳的编辑器支持。处处皆可自动补全，减少调试时间。
  • 简单：设计的易于使用和学习，阅读文档的时间更短。
  • 简短：使代码重复最小化。通过不同的参数声明实现丰富功能。bug 更少。
  • 健壮：生产可用级别的代码。还有自动生成的交互式文档。
  • 标准化：基于（并完全兼容）API 的相关开放标准：OpenAPI (以前被称为 Swagger)
    和 JSON Schema。

* 根据对某个构建线上应用的内部开发团队所进行的测试估算得出。}

%description %{common_description_en}

%description -l de %{common_description_de}

%description -l en %{common_description_en}

%description -l es %{common_description_es}

%description -l fa %{common_description_fa}

%description -l fr %{common_description_fr}

%description -l ja %{common_description_ja}

%description -l ko %{common_description_ko}

%description -l pt %{common_description_pt}

%description -l ru %{common_description_ru}

%description -l tr %{common_description_tr}

%description -l uk %{common_description_uk}

%description -l vi %{common_description_vi}

%description -l zh-Hant %{common_description_zh_hant}

%description -l zh %{common_description_zh}


%package -n     python3-fastapi
Summary:        %{sum_en}

Summary(de):    %{sum_de}
Summary(en):    %{sum_en}
Summary(es):    %{sum_es}
Summary(fa):    %{sum_fa}
Summary(fr):    %{sum_fr}
Summary(ja):    %{sum_ja}
Summary(ko):    %{sum_ko}
Summary(pt):    %{sum_pt}
Summary(ru):    %{sum_ru}
Summary(tr):    %{sum_tr}
Summary(uk):    %{sum_uk}
Summary(vi):    %{sum_vi}
Summary(zh-Hant):    %{sum_zh_hant}
Summary(zh):    %{sum_zh}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-fastapi-slim = %{version}-%{release}

%description -n python3-fastapi %{common_description_en}

%description -n python3-fastapi -l de %{common_description_de}

%description -n python3-fastapi -l en %{common_description_en}

%description -n python3-fastapi -l es %{common_description_es}

%description -n python3-fastapi -l fa %{common_description_fa}

%description -n python3-fastapi -l fr %{common_description_fr}

%description -n python3-fastapi -l ja %{common_description_ja}

%description -n python3-fastapi -l ko %{common_description_ko}

%description -n python3-fastapi -l pt %{common_description_pt}

%description -n python3-fastapi -l ru %{common_description_ru}

%description -n python3-fastapi -l tr %{common_description_tr}

%description -n python3-fastapi -l uk %{common_description_uk}

%description -n python3-fastapi -l vi %{common_description_vi}

%description -n python3-fastapi -l zh-Hant %{common_description_zh_hant}

%description -n python3-fastapi -l zh %{common_description_zh}


%pyproject_extras_subpkg -n python3-fastapi -i %{python3_sitelib}/fastapi-%{version}.dist-info all


%package -n     python3-fastapi-slim
Summary:        %{sum_en}

Summary(de):    %{sum_de}
Summary(en):    %{sum_en}
Summary(es):    %{sum_es}
Summary(fa):    %{sum_fa}
Summary(fr):    %{sum_fr}
Summary(ja):    %{sum_ja}
Summary(ko):    %{sum_ko}
Summary(pt):    %{sum_pt}
Summary(ru):    %{sum_ru}
Summary(tr):    %{sum_tr}
Summary(uk):    %{sum_uk}
Summary(vi):    %{sum_vi}
Summary(zh-Hant):    %{sum_zh_hant}
Summary(zh):    %{sum_zh}

%description -n python3-fastapi-slim %{common_description_en}

%description -n python3-fastapi-slim -l de %{common_description_de}

%description -n python3-fastapi-slim -l en %{common_description_en}

%description -n python3-fastapi-slim -l es %{common_description_es}

%description -n python3-fastapi-slim -l fa %{common_description_fa}

%description -n python3-fastapi-slim -l fr %{common_description_fr}

%description -n python3-fastapi-slim -l ja %{common_description_ja}

%description -n python3-fastapi-slim -l ko %{common_description_ko}

%description -n python3-fastapi-slim -l pt %{common_description_pt}

%description -n python3-fastapi-slim -l ru %{common_description_ru}

%description -n python3-fastapi-slim -l tr %{common_description_tr}

%description -n python3-fastapi-slim -l uk %{common_description_uk}

%description -n python3-fastapi-slim -l vi %{common_description_vi}

%description -n python3-fastapi-slim -l zh-Hant %{common_description_zh_hant}

%description -n python3-fastapi-slim -l zh %{common_description_zh}


%pyproject_extras_subpkg -n python3-fastapi-slim -i %{python3_sitelib}/fastapi_slim-%{version}.dist-info standard all standard-no-fastapi-cloud-cli


%prep
%autosetup -n fastapi-%{version} -p1

%if %{with bootstrap}
# Break a dependency cycle with fastapi-cli by commenting out all dependencies
# on it. Note that this removes it from the “standard”,
# “standard-no-fastapi-cloud-cli”, and “all” extras metapackages.
sed -r -i 's/("fastapi-cli(-slim)?\b.*",)/# \1/' pyproject.toml
%endif
%if %{without orjson}
# Comment out all dependencies on orjson (for ORJSONResponse). Note that this
# removes it from the “all” extra metapackage.
sed -r -i 's/("orjson\b.*",)/# \1/' pyproject.toml
%endif
%if %{without uvicorn}
# Comment out all dependencies on uvicorn. Note that this removes it from the
# “all” extra metapackage.
sed -r -i 's/("uvicorn\b.*",)/# \1/' pyproject.toml
%endif
%if %{without inline_snapshot}
# Stub out inline_snapshot.Snapshot so that tests/utils.py is still importable;
# the pydantic_snapshot function will still fail if it ever actually *called*.
sed -r -i 's/from inline_snapshot import Snapshot/# &\nSnapshot = object/' \
    tests/utils.py
%endif

# Remove bundled js-termynal 0.0.1; since we are not building documentation, we
# do this very bluntly:
rm -rvf docs/*/docs/js docs/*/docs/css


%generate_buildrequires
export TIANGOLO_BUILD_PACKAGE='fastapi-slim'
%pyproject_buildrequires -x standard,all,standard-no-fastapi-cloud-cli
(
  export TIANGOLO_BUILD_PACKAGE='fastapi'
  %pyproject_buildrequires -x all
) | grep -vE '\bfastapi-slim\b'


%build
export TIANGOLO_BUILD_PACKAGE='fastapi-slim'
%pyproject_wheel
export TIANGOLO_BUILD_PACKAGE='fastapi'
%pyproject_wheel


%install
%pyproject_install

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}' \
    '%{SOURCE15}'

install -d \
    '%{buildroot}%{bash_completions_dir}' \
    '%{buildroot}%{zsh_completions_dir}' \
    '%{buildroot}%{fish_completions_dir}'
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
export _TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION=1
'%{buildroot}%{_bindir}/fastapi' --show-completion bash \
    > '%{buildroot}%{bash_completions_dir}/fastapi'
'%{buildroot}%{_bindir}/fastapi' --show-completion zsh \
    > '%{buildroot}%{zsh_completions_dir}/_fastapi'
'%{buildroot}%{_bindir}/fastapi' --show-completion fish \
    > '%{buildroot}%{fish_completions_dir}/fastapi.fish'


%check
%if %{with bootstrap}
ignore="${ignore-} --ignore=tests/test_fastapi_cli.py"
%endif

%if %{without inline_snapshot}
ignore="${ignore-} --ignore-glob=tests/test_tutorial/test_cookie_param_models/*"
ignore="${ignore-} --ignore-glob=tests/test_tutorial/test_header_param_models/*"
ignore="${ignore-} --ignore-glob=tests/test_tutorial/test_query_param_models/*"
ignore="${ignore-} --ignore=tests/test_tutorial/test_query_params_str_validations/test_tutorial015.py"
%endif

%if %{without orjson}
k="${k-}${k+ and }not test_orjson_non_str_keys"
ignore="${ignore-} --ignore=tests/test_default_response_class.py"
ignore="${ignore-} --ignore=tests/test_tutorial/test_custom_response/test_tutorial001b.py"
ignore="${ignore-} --ignore=tests/test_tutorial/test_custom_response/test_tutorial009c.py"
%endif

%if %{without pyjwt}
ignore="${ignore-} --ignore-glob=tests/test_tutorial/test_security/test_tutorial005*"
%endif

%if %[ %{without sqlmodel} || %{without inline_snapshot} ]
ignore="${ignore-} --ignore-glob=tests/test_tutorial/test_sql_databases/*"
%endif

# Ignore all DeprecationWarning messages, as they pop up from various
# dependencies in practice. Upstream deals with this by tightly controlling
# dependency versions in CI.
warningsfilter="${warningsfilter-} -W ignore::DeprecationWarning"

%pytest ${warningsfilter-} -k "${k-}" ${ignore-}


%files -n python3-fastapi
%{python3_sitelib}/fastapi-%{version}.dist-info/


%files -n python3-fastapi-slim
%license LICENSE
%doc CITATION.cff
%doc README.md

%{python3_sitelib}/fastapi/
%{python3_sitelib}/fastapi_slim-%{version}.dist-info/

# Based on testing in a virtualenv, the upstream behavior is that the fastapi
# CLI tool is installed with all “flavors” of fastapi, including fastapi-slim;
# it relies on the “standard” extra to be useful, and prints the following if
# the requisite extra is not installed:
#   To use the fastapi command, please install "fastapi[standard]":
#           pip install "fastapi[standard]"
#   Traceback (most recent call last):
#     […]
# By installing the entry point with the fastapi-slim package, we imitate the
# upstream behavior.
%{_bindir}/fastapi
%{_mandir}/man1/fastapi.1*
%{_mandir}/man1/fastapi-*.1*
%{bash_completions_dir}/fastapi
%{zsh_completions_dir}/_fastapi
%{fish_completions_dir}/fastapi.fish


%changelog
%autochangelog
