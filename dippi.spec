%global appname com.github.cassidyjames.dippi

Name:           dippi
Summary:        Calculate display info like DPI and aspect ratio
Version:        3.1.4
Release:        %autorelease
# The entire source is GPL-3.0-only, except:
#   - data/metadata.appdata.xml.in is CC0-1.0, which is allowed for content
#     only
License:        GPL-3.0-only AND CC0-1.0

URL:            https://github.com/cassidyjames/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.0.0

Requires:       hicolor-icon-theme

Summary(en_AU): Calculate display info like DPI and aspect ratio
Summary(en_CA): Calculate display info like DPI and aspect ratio
Summary(en_GB): Calculate display info like DPI and aspect ratio
Summary(es):    Cálculo de datos de la pantalla como los PPP y la relación de aspecto
Summary(fr_CA): Calculez les informations de l’écran comme le DPI ou le ratio
Summary(fr):    Calculez les informations de l’écran comme le DPI ou le ratio
Summary(lt):    Apskaičiuoti tokią ekrano informaciją kaip taškus colyje (DPI) ir proporcijas
Summary(nl):    Bereken scherminformatie, zoals DPI en beeldverhouding
Summary(pt):    Calcule informação do monitor como o DPI e a relação de aspeto
Summary(tr):    DPI ve en boy oranı gibi ekran bilgilerini hesaplama


%description
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiate between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Based on the author’s expertise and experience shipping HiDPI hardware and
software at System76 and elementary.

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l en_AU
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiates between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Based on the author’s expertise and experience shipping HiDPI hardware and
software at System76 and elementary.

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l en_CA
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiates between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Based on the author’s expertise and experience shipping HiDPI hardware and
software at System76 and elementary.

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l en_GB
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiates between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Based on the expertise of Cassidy James Blaede and the actual logic System76
uses to determine screen size and resolution combinations.

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l es
Análisis de cualquier pantalla. Proporcione unos pocos datos y averigüe la
relación de aspecto, los PPP y otros detalles sobre una pantalla concreta.
Estupendo para decidir qué portátil o monitor externo comprar y si este
puede considerarse de alta resolución.

Funcionalidades útiles:
  • Descubra si una pantalla es una buena elección en función de su tamaño y su
    resolución
  • Obtenga orientaciones sobre las distintas densidades
  • Conozca la resolución lógica
  • Distinga las pantallas para portátiles de las de escritorio
  • Sencillísimo: todo en una ventanita

Basada en los conocimientos técnicos de Cassidy James Blaede y la lógica que
System76 emplea para verificar combinaciones de tamaño y resolución en las
pantallas.

Le dice si la densidad de una pantalla es:
  • de muy pocos PPP,
  • de PPP relativamente escasos,
  • ideal para resolución baja,
  • potencialmente problemática,
  • ideal para resolución alta,
  • bastante elevada para resolución alta, o
  • de PPP demasiado elevados

%description -l fr_CA
Analysez n’importe quel écran. Entrez de simples détails à son propos et
obtenez son ratio, son DPI, et d’autres détails. Ainsi, vous pourrez plus
aisément décider quel ordinateur portable ou écran acheter, et savoir si il
sera considéré comme HiDPI.

Fonctionnalités utiles:
  • Déterminez si un écran est un bon choix en vous basant sur sa diagonale et
    sa résolution
  • Obtenez des conseils sur différentes densités d’écran
  • Apprendre la résolution logique
  • Différencie les écrans d’ordinateurs de bureau et portables
  • Stupidement simple: tout dans une p’tite fenêtre toute mignone

Basé sur l’expertise de Cassidy James Blaede et sur la logique que System76
utilise pour déterminer la résolution et la diagonale d’écran.

Vous dit si la densité d’un écran a:
  • DPI très faible
  • DPI plutôt faible
  • Densité idéale pour le LoDPI
  • DPI potentiellement problèmatique
  • Densité idéale pour le HiDPI
  • Densité plutôt haute pour le HiDPI, ou
  • DPI trop haut

%description -l fr
Analysez n’importe quel écran. Entrez de simples détails à son propos et
obtenez son ratio, son DPI, et d’autres détails. Ainsi, vous pourrez plus
aisément décider quel ordinateur portable ou écran acheter, et savoir si il
sera considéré comme HiDPI.

Fonctionnalités utiles:
  • Déterminez si un écran est un bon choix en vous basant sur sa diagonale et
    sa résolution
  • Obtenez des conseils sur différentes densités d’écran
  • Apprendre la résolution logique
  • Différencie les écrans d’ordinateurs de bureau et portables
  • Stupidement simple: tout dans une p’tite fenêtre toute mignone

Basé sur l’expertise de Cassidy James Blaede et sur la logique que System76
utilise pour déterminer la résolution et la diagonale d’écran.

Vous dit si la densité d’un écran a:
  • DPI très faible
  • DPI plutôt faible
  • Densité idéale pour le LoDPI
  • DPI potentiellement problèmatique
  • Densité idéale pour le HiDPI
  • Densité plutôt haute pour le HiDPI, ou
  • DPI trop haut

%description -l lt
Išanalizuokite bet kurį ekraną. Įveskite kai kurią paprastą informaciją ir
sužinokite proporcijas, taškus colyje (DPI) ir kitą tam tikro ekrano
informaciją. Puikiai tinka sprendžiant kurį nešiojamąjį kompiuterį ar išorinį
ekraną įsigyti, ir ar jis bus laikomas HiDPI.

Naudingos ypatybės:
  • Sužinokite ar ekranas pagal savo dydį ir raišką yra geras pasirinkimas
  • Gaukite patarimus apie įvairius tankius
  • Sužinokite loginę raišką
  • Atskirkite nešiojamųjų ir stalinių kompiuterių ekranus
  • Kvailai paprasta:  viskas viename mažame lange

Paremta Cassidy James Blaede kompetencija ir tikraisiais loginiais System76
naudojimais, skirtais nustatyti ekrano dydžio ir raiškos kombinacijas.

Nurodo ar ekrano tankis yra:
  • Labai žemo DPI,
  • Pakankamai žemo DPI,
  • Idealus LoDPI,
  • Galimai problematiškas,
  • Idealus HiDPI,
  • Pakankamai didelis HiDPI ar
  • Per didelio DPI

%description -l nl
Analyseer welk scherm dan ook. Voer een paar eenvoudige gegevens in en bereken
de beeldverhouding, DPI en andere schermgegevens. Handig bij het bepalen welke
laptop of externe monitor je wilt kopen en of het scherm in kwestie HiDPI is.

Handige functies:
  • Bepaal of een scherm een goede aankoop zou zijn, op basis van grootte en
    resolutie
  • Verkrijg advies over verschillende dichtheden
  • Verkrijg informatie over logische resolutie
  • Onderscheid tussen laptop- en desktopschermen
  • Eenvoudiger kan niet: alles in een klein, handig venster

Gebaseerd op de expertise van Cassidy James Blaede en de techniek die System76
gebruikt bij het bepalen van de combinatie van schermgrootte en resolutie.

Toont je of de schermdichtheid:
  • Erg laag is,
  • Redelijk laag,
  • Ideaal voor LoDPI,
  • Wellicht problematisch,
  • Ideaal voor HiDPI,
  • Redelijk hoog voor HiDPI of
  • Té hoog

%description -l pt
Analisa um monitor qualquer. Insira alguns detalhes simples e descubra a
relação de aspeto, DPI e outros detalhes de um monitor em particular. É ótimo
para decidir qual o computador portátil ou monitor a comprar e se é considerado
HiDPI.

Funcionalidades úteis:
  • Descubra se o monitor é a escolha correta baseando-se no seu tamanho e
    resolução
  • Obtenha conselhos sobre densidades diferentes
  • Aprenda a resolução lógica
  • Diferencie entre computadores portáteis e monitores de secretária
  • Estupidamente simples: tudo numa pequena e engraçada janela

Baseado na experiência de Cassidy James Blaede e na lógica em si que o System76
usa para determinar combinações de tamanho do ecrã e resolução.

Diz-lhe se a densidade do monitor é:
  • DPI Muito Baixo,
  • DPI Baixo,
  • Ideal para LoDPI,
  • Potencialmente Problemático
  • Ideal para HiDPI,
  • Razoavelmente Alto para HiDPI, ou
  • DPI Demasiado Alto

%description -l tr
Herhangi bir ekranı analiz edin. Birkaç basit ayrıntı girin ve en boy oranını,
DPI'yi ve belirli bir ekranın diğer ayrıntılarını bulun. Hangi dizüstü
bilgisayarın veya harici monitörün satın alınacağına ve HiDPI olarak kabul
edilip edilmeyeceğine karar vermek için harika bir uygulama.

Kullanışlı özellikler:
  • Bir ekranın boyutuna ve çözünürlüğüne göre iyi bir seçim olup olmadığını öğrenin
  • Farklı yoğunluklar hakkında tavsiye alın
  • Mantıksal çözünürlüğü öğrenin
  • Dizüstü bilgisayarlar ve masaüstü ekranları arasında ayrım yapın
  • Kısaca:Hepsi zarif bir pencere

Cassidy James Blaede'nin uzmanlığına ve gerçek mantığa dayanarak System76'nın
ekran boyutu ve çözünürlüğünü belirtmek için kullanılan uygulama.

Bir ekranın yoğunluğunu:
  • Çok Düşük DPI,
  • Oldukça Düşük DPI,
  • LoDPI için ideal,
  • Potansiyel Olarak Sorunlu,
  • HiDPI için ideal,
  • HiDPI için Oldukça Yüksek veya
  • Çok Yüksek DPI


%prep
%autosetup

# While https://github.com/cassidyjames/dippi/issues/82 is fixed upstream, the
# typo is still present in non-US English localizations—shall we say
# localisations?
sed -r -i 's/(display)‘s/\1’s/g' po/en_*.po


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml
# Matches what gnome-software and others use:
appstreamcli validate --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_metainfodir}/%{appname}.appdata.xml


%changelog
%autochangelog
