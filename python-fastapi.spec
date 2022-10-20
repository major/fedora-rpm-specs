# For translations, check docs/*/docs/index.md
# Note that there are many other localized versions of the documentation
# *present*, but untranslated.
%global sum_en  FastAPI framework
%global sum_es  FastAPI framework
%global sum_he  תשתית FastAPI
%global sum_ja  FastAPI framework
%global sum_ko  FastAPI 프레임워크
%global sum_pl  FastAPI to szybki
%global sum_pt  Framework FastAPI
%global sum_tr  FastAPI framework
%global sum_zh  FastAPI 框架

Name:           python-fastapi
Version:        0.79.0
Release:        %autorelease
Summary:        %{sum_en}

License:        MIT
URL:            https://github.com/tiangolo/fastapi
Source0:        %{url}/archive/%{version}/fastapi-%{version}.tar.gz
BuildArch:      noarch

# Bump starlette to 0.20.4
# https://github.com/tiangolo/fastapi/pull/5172
Patch:          %{url}/pull/5172.patch

# Fix sql_app_py39 and py310 tests
# https://github.com/tiangolo/fastapi/pull/4409
Patch:          %{url}/pull/4409.patch

# Ignore Python 3.11-related deprecation warnings that bubble up from httpx and
# are treated as errors. This might be suitable for submission upstream, but it
# will be easier to get it looked at when more of FastAPI’s dependencies
# officially support Python 3.11.
Patch:          fastapi-0.78.0-httpx-cgi-deprecation.patch

BuildRequires:  python3-devel

Obsoletes:      python-fastapi-doc < 0.68.1-6

Summary(en):    %{sum_en}
Summary(es):    %{sum_es}
Summary(he):    %{sum_he}
Summary(ja):    %{sum_ja}
Summary(ko):    %{sum_ko}
Summary(pl):    %{sum_pl}
Summary(pt):    %{sum_pt}
Summary(tr):    %{sum_tr}
Summary(zh):    %{sum_zh}

%global common_description_en %{expand:
FastAPI is a modern, fast (high-performance), web framework for building APIs
with Python 3.6+ based on standard Python type hints.

The key features are:

  • Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette
    and Pydantic). One of the fastest Python frameworks available.

  • Fast to code: Increase the speed to develop features by about 200% to 300%.*
  • Fewer bugs: Reduce about 40% of human (developer) induced errors.*
  • Intuitive: Great editor support. Completion everywhere. Less time
    debugging.
  • Easy: Designed to be easy to use and learn. Less time reading docs.
  • Short: Minimize code duplication. Multiple features from each parameter
    declaration. Fewer bugs.
  • Robust: Get production-ready code. With automatic interactive
    documentation.
  • Standards-based: Based on (and fully compatible with) the open standards
    for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

* estimation based on tests on an internal development team, building production
  applications.}
%global common_description_es %{expand:
FastAPI es un web framework moderno y rápido (de alto rendimiento) para
construir APIs con Python 3.6+ basado en las anotaciones de tipos estándar de
Python.

Sus características principales son:

  • Rapidez: Alto rendimiento, a la par con NodeJS y Go (gracias a
    Starlette y Pydantic). Uno de los frameworks de Python más rápidos.

  • Rápido de programar: Incrementa la velocidad de desarrollo entre 200% y
    300%.*
  • Menos errores: Reduce los errores humanos (de programador) aproximadamente
    un 40%.*
  • Intuitivo: Gran soporte en los editores con auto completado en todas
    partes. Gasta menos tiempo debugging.
  • Fácil: Está diseñado para ser fácil de usar y aprender. Gastando menos
    tiempo leyendo documentación.
  • Corto: Minimiza la duplicación de código. Múltiples funcionalidades con
    cada declaración de parámetros. Menos errores.
  • Robusto: Crea código listo para producción con documentación automática
    interactiva.
  • Basado en estándares: Basado y totalmente compatible con los estándares
    abiertos para APIs: OpenAPI (conocido previamente como Swagger) y JSON
    Schema.

* Esta estimación está basada en pruebas con un equipo de desarrollo interno
  contruyendo aplicaciones listas para producción.}
%global common_description_he %{expand:
FastAPI היא תשתית רשת מודרנית ומהירה (ביצועים גבוהים) לבניית ממשקי תכנות
יישומים (API) עם פייתון 3.6+ בהתבסס על רמזי טיפוסים סטנדרטיים.

תכונות המפתח הן:

  • מהירה: ביצועים גבוהים מאוד, בקנה אחד עם NodeJS ו - Go (תודות ל - Starlette
  • ו - Pydantic). אחת מתשתיות הפייתון המהירות ביותר.

  • מהירה לתכנות: הגבירו את מהירות פיתוח התכונות החדשות בכ - %200 עד %300.*
  • פחות שגיאות: מנעו כ - %40 משגיאות אנוש (מפתחים).*
  • אינטואיטיבית: תמיכת עורך מעולה. השלמה בכל מקום. פחות זמן ניפוי שגיאות.
  • קלה: מתוכננת להיות קלה לשימוש וללמידה. פחות זמן קריאת תיעוד.
  • קצרה: מזערו שכפול קוד. מספר תכונות מכל הכרזת פרמטר. פחות שגיאות.
  • חסונה: קבלו קוד מוכן לסביבת ייצור. עם תיעוד אינטרקטיבי אוטומטי.
  • מבוססת סטנדרטים: מבוססת על (ותואמת לחלוטין ל -) הסטדנרטים הפתוחים לממשקי
    תכנות יישומים: OpenAPI (ידועים לשעבר כ - Swagger) ו - JSON Schema.

* הערכה מבוססת על בדיקות של צוות פיתוח פנימי שבונה אפליקציות בסביבת ייצור.}
%global common_description_ja %{expand:
FastAPI は、Pythonの標準である型ヒントに基づいてPython 3.6 以降でAPI
を構築するための、モダンで、高速(高パフォーマンス)な、Web フレームワークです。

主な特徴:

  - 高速: NodeJS や Go 並みのとても高いパフォーマンス (Starlette と Pydantic
    のおかげです)。最も高速な Python フレームワークの一つです。

  - 高速なコーディング: 開発速度を約 200%~300%向上させます。 *
  - 少ないバグ: 開発者起因のヒューマンエラーを約 40％削減します。 *
  - 直感的: 素晴らしいエディタのサポートや オートコンプリート。
    デバッグ時間を削減します。
  - 簡単: 簡単に利用、習得できるようにデザインされています。
    ドキュメントを読む時間を削減します。
  - 短い: コードの重複を最小限にしています。
    各パラメータからの複数の機能。少ないバグ。
  - 堅牢性:
    自動対話ドキュメントを使用して、本番環境で使用できるコードを取得します。
  - Standards-based: API
    のオープンスタンダードに基づいており、完全に互換性があります: OpenAPI
    (以前は Swagger として知られていました) や JSON スキーマ.

* 本番アプリケーションを構築している開発チームのテストによる見積もり。}
%global common_description_ko %{expand:
FastAPI는 현대적이고, 빠르며(고성능), 파이썬 표준 타입 힌트에 기초한
Python3.6+의 API를 빌드하기 위한 웹 프레임워크입니다.

주요 특징으로:

  • 빠름: (Starlette과 Pydantic 덕분에) NodeJS 및 Go와 대등할 정도로 매우 높은
    성능. 사용 가능한 가장 빠른 파이썬 프레임워크 중 하나.

  • 빠른 코드 작성: 약 200%에서 300%까지 기능 개발 속도 증가.*
  • 적은 버그: 사람(개발자)에 의한 에러 약 40% 감소.*
  • 직관적: 훌륭한 편집기 지원. 모든 곳에서 자동완성. 적은 디버깅 시간.
  • 쉬움: 쉽게 사용하고 배우도록 설계. 적은 문서 읽기 시간.
  • 짧음: 코드 중복 최소화. 각 매개변수 선언의 여러 기능. 적은 버그.
  • 견고함: 준비된 프로덕션 용 코드를 얻으십시오. 자동 대화형 문서와 함께.
  • 표준 기반: API에 대한 (완전히 호환되는) 개방형 표준 기반: OpenAPI (이전에
    Swagger로 알려졌던) 및 JSON 스키마.

* 내부 개발팀의 프로덕션 애플리케이션을 빌드한 테스트에 근거한 측정}
%global common_description_pl %{expand:
FastAPI to nowoczesny, wydajny framework webowy do budowania API z użyciem
Pythona 3.6+ bazujący na standardowym typowaniu Pythona.

Kluczowe cechy:

  • Wydajność: FastAPI jest bardzo wydajny, na równi z NodeJS oraz Go (dzięki
    Starlette i Pydantic). Jeden z najszybszych dostępnych frameworków
    Pythonowych.
  • Szybkość kodowania: Przyśpiesza szybkość pisania nowych funkcjonalności o
    około 200% do 300%.*
  • Mniejsza ilość błędów: Zmniejsza ilość ludzkich (dewelopera) błędy o około
    40%.*
  • Intuicyjność: Wspaniałe wsparcie dla edytorów kodu. Dostępne wszędzie
    automatyczne uzupełnianie kodu. Krótszy czas debugowania.
  • Łatwość: Zaprojektowany by być prosty i łatwy do nauczenia. Mniej czasu
    spędzonego na czytanie dokumentacji.
  • Kompaktowość: Minimalizacja powtarzającego się kodu. Wiele funkcjonalności
    dla każdej deklaracji parametru. Mniej błędów.
  • Solidność: Kod gotowy dla środowiska produkcyjnego. Wraz z automatyczną
    interaktywną dokumentacją.
  • Bazujący na standardach: Oparty na (i w pełni kompatybilny z) otwartych
    standardach API: OpenAPI (wcześniej znane jako Swagger) oraz JSON Schema.

* oszacowania bazowane na testach wykonanych przez wewnętrzny zespół
  deweloperów, budujących aplikacie używane na środowisku produkcyjnym.}
%global common_description_pt %{expand:
FastAPI é um moderno e rápido (alta performance) framework web para construção
de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python.

Os recursos chave são:

  • Rápido: alta performance, equivalente a NodeJS e Go (graças ao Starlette e
    Pydantic). Um dos frameworks mais rápidos disponíveis.
  • Rápido para codar: Aumenta a velocidade para desenvolver recursos entre
    200% a 300%.*
  • Poucos bugs: Reduz cerca de 40% de erros induzidos por humanos
    (desenvolvedores).*
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
%global common_description_tr %{expand:
FastAPI, Python 3.6+'nın standart type hintlerine dayanan modern ve hızlı
(yüksek performanslı) API'lar oluşturmak için kullanılabilecek web framework'ü.

Ana özellikleri:

  • Hızlı: çok yüksek performanslı, NodeJS ve Go ile eşdeğer seviyede
  performans sağlıyor, (Starlette ve Pydantic sayesinde.) Python'un en hızlı
  frameworklerinden bir tanesi.

  • Kodlaması hızlı: Yeni özellikler geliştirmek neredeyse %200 - %300 daha hızlı.*
  • Daha az bug: Geliştirici (insan) kaynaklı hatalar neredeyse %40 azaltıldı.*
  • Sezgileri güçlü: Editor (otomatik-tamamlama) desteği harika. Otomatik
    tamamlama her yerde. Debuglamak ile daha az zaman harcayacaksınız.
  • Kolay: Öğrenmesi ve kullanması kolay olacak şekilde. Doküman okumak için
    harcayacağınız süre azaltıldı.
  • Kısa: Kod tekrarını minimuma indirdik. Fonksiyon parametrelerinin tiplerini
    belirtmede farklı yollar sunarak karşılaşacağınız bug'ları azalttık.
  • Güçlü: Otomatik dokümantasyon ile beraber, kullanıma hazır kod yaz.
  • Standartlar belirli: Tamamiyle API'ların açık standartlara bağlı ve (tam
    uyumlululuk içerisinde); OpenAPI (eski adıyla Swagger) ve JSON Schema.

* Bahsi geçen rakamsal ifadeler tamamiyle, geliştirme takımının kendi
  sundukları ürünü geliştirirken yaptıkları testlere dayanmakta.}
%global common_description_zh %{expand:
FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+
并基于标准的 Python 类型提示。

关键特性:

  • 快速：可与 NodeJS 和 Go 比肩的极高性能（归功于 Starlette 和 Pydantic）。
    最快的 Python web 框架之一。
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

%description -l en %{common_description_en}
%description -l es %{common_description_es}
%description -l he %{common_description_he}
%description -l ja %{common_description_ja}
%description -l ko %{common_description_ko}
%description -l pl %{common_description_pl}
%description -l pt %{common_description_pt}
%description -l tr %{common_description_tr}
%description -l zh %{common_description_zh}


%pyproject_extras_subpkg -n python3-fastapi all


%package -n     python3-fastapi
Summary:        %{sum_en}

Summary(en):    %{sum_en}
Summary(es):    %{sum_es}
Summary(he):    %{sum_he}
Summary(ja):    %{sum_ja}
Summary(ko):    %{sum_ko}
Summary(pl):    %{sum_pl}
Summary(pt):    %{sum_pt}
Summary(tr):    %{sum_tr}
Summary(zh):    %{sum_zh}

%description -n python3-fastapi %{common_description_en}

%description -n python3-fastapi -l en %{common_description_en}
%description -n python3-fastapi -l es %{common_description_es}
%description -n python3-fastapi -l he %{common_description_he}
%description -n python3-fastapi -l ja %{common_description_ja}
%description -n python3-fastapi -l ko %{common_description_ko}
%description -n python3-fastapi -l pl %{common_description_pl}
%description -n python3-fastapi -l pt %{common_description_pt}
%description -n python3-fastapi -l tr %{common_description_tr}
%description -n python3-fastapi -l zh %{common_description_zh}


%prep
%autosetup -n fastapi-%{version} -p1

# Comment out all dependencies on orjson (for ORJSONResponse); it cannot be
# packaged in Fedora until it builds with the stable Rust toolchain instead of
# the nightly one. Note that this removes it from the “all” extra metapackage.
sed -r -i 's/("orjson\b.*",)/# \1/' pyproject.toml
# Comment out test dependencies that are only for linting/formatting/analysis,
# and will not be used. Also comment out the “dev” dependency on pre-commit,
# which we will not use here.
sed -r -i 's/("(mypy|black|flake8|isort|autoflake|pre-commit)\b.*",)/# \1/' \
    pyproject.toml
# We won’t be running a type checker (mypy), so we don’t need any
# auto-generated PEP 561 stub packages:
sed -r -i 's/("types-(u|or)json\b.*",)/# \1/' pyproject.toml
# Selectively allow newer versions for certain tightly-pinned dependencies:
sed -r -i 's/("((databases|httpx|pytest)\b)[^<"]*),[[:blank:]]*<[^"]*/\1/' \
    pyproject.toml

# Remove bundled js-termynal 0.0.1; since we are not building documentation, we
# do this very bluntly:
rm -rvf docs/*/docs/js docs/*/docs/css


%generate_buildrequires
%pyproject_buildrequires -x all,test,dev


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fastapi


%check
# Requires orjson:
#   tests/test_tutorial/test_custom_response/test_tutorial001b.py
#   tests/test_default_response_class.py
%pytest \
    --ignore=tests/test_tutorial/test_custom_response/test_tutorial001b.py \
    --ignore=tests/test_default_response_class.py


%files -n python3-fastapi -f %{pyproject_files}
%license LICENSE
%doc CONTRIBUTING.md
%doc README.md


%changelog
%autochangelog
