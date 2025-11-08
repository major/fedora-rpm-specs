%global appname com.cassidyjames.dippi

Name:           dippi
Summary:        Calculate display info like DPI and aspect ratio
Version:        4.2.0
Release:        %autorelease
# The entire source is GPL-3.0-only, except:
#   - data/metadata.metainfo.xml.in is CC0-1.0, which is allowed for content
#     only
License:        GPL-3.0-only AND CC0-1.0

URL:            https://github.com/cassidyjames/dippi
Source:         %{url}/archive/%{version}/dippi-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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

BuildRequires:  pkgconfig(gtk4) >= 4.19.4
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8.1

Requires:       hicolor-icon-theme

Summary(en_AU): Calculate display info like DPI and aspect ratio
Summary(en_CA): Calculate display info like DPI and aspect ratio
Summary(en_GB): Calculate display info like DPI and aspect ratio
Summary(es):    Cálculo de datos de la pantalla como los PPP y la relación de aspecto
Summary(fr_CA): Calculez les informations de l’écran comme le DPI ou le ratio
Summary(fr):    Calculez des informations sur l'écran comme le DPI ou le ratio
Summary(it):    Calcola le informazioni di visualizzazione come DPI
Summary(lt):    Apskaičiuoti tokią ekrano informaciją kaip taškus colyje (DPI) ir proporcijas
Summary(nl):    Bereken scherminformatie, zoals DPI en beeldverhouding
Summary(pt):    Calcule informação do monitor como o DPI e a relação de aspeto
Summary(tr):    DPI ve en boy oranı gibi ekran bilgilerini hesaplama


%description
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Lots of handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiate between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l en_AU
Analyse any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Lots of handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiates between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

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

Lots of handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiates between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

Tells you if a display’s density is:
  • Very Low DPI,
  • Fairly Low DPI,
  • Ideal for LoDPI,
  • Potentially Problematic,
  • Ideal for HiDPI,
  • Fairly High for HiDPI, or
  • Too High DPI

%description -l en_GB
Analyse any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Lots of handy features:
  • Find out if a display is a good choice based on its size and resolution
  • Get advice about different densities
  • Learn the logical resolution
  • Differentiates between laptops and desktop displays
  • Stupid simple: all in a cute li’l window

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

Vous dit si la densité d’un écran a:
  • DPI très faible
  • DPI plutôt faible
  • Densité idéale pour le LoDPI
  • DPI potentiellement problèmatique
  • Densité idéale pour le HiDPI
  • Densité plutôt haute pour le HiDPI, ou
  • DPI trop haut

%description -l fr
Analysez n’importe quel écran. Saisissez quelques informations simples et
découvrez le ratio d’aspect, le DPI et d’autres détails d’un écran
particulier. Idéal pour décider de l’achat d’un ordinateur portable ou d’un
écran externe, et pour savoir s’il est considéré comme HiDPI.

Fonctionnalités pratiques :
  • Déterminer si un écran est un bon choix en vous basant sur sa diagonale et
    sa résolution
  • Obtenez des conseils sur les différentes densités
  • Apprendre la résolution logique
  • Différencier les écrans d’ordinateurs de bureau et laptops
  • Stupidement simple : tout dans une jolie p’tite fenêtre toute mignonne

Vous dit si la densité d’un écran est :
  • à DPI très bas,
  • à DPI assez bas,
  • Idéale pour LoDPI,
  • Potentiellement problématique,
  • Idéale pour HiDPI,
  • assez haute pour HiDPI, ou
  • DPI trop haut

%description -l it
Analizza qualsiasi display. Inserisci alcuni semplici dettagli e scopri le
proporzioni, il DPI e altri dettagli di un particolare display. Ottimo per
decidere quale laptop o monitor esterno acquistare e se sarebbe considerato
HiDPI.

Funzioni utili:
  • Scopri se un display è una buona scelta in base alle sue dimensioni e
    risoluzione
  • Ottieni consigli sulle diverse densità
  • Impara la risoluzione logica
  • Distinguere tra laptop e display desktop
  • Stupido e semplice: tutto in una graziosa finestrella

Ti dice se la densità di un display è:
  • DPI molto basso,
  • DPI abbastanza basso,
  • Ideale per LoDPI,
  • Potenzialmente problematico,
  • Ideale per HiDPI,
  • Abbastanza alto per HiDPI, o
  • DPI troppo alto

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
  • Bir ekranın boyutuna ve çözünürlüğüne göre iyi bir seçim olup olmadığını
    öğrenin
  • Farklı yoğunluklar hakkında tavsiye alın
  • Mantıksal çözünürlüğü öğrenin
  • Dizüstü bilgisayarlar ve masaüstü ekranları arasında ayrım yapın
  • Kısaca:Hepsi zarif bir pencere

Bir ekranın yoğunluğunu:
  • Çok Düşük DPI,
  • Oldukça Düşük DPI,
  • LoDPI için ideal,
  • Potansiyel Olarak Sorunlu,
  • HiDPI için ideal,
  • HiDPI için Oldukça Yüksek veya
  • Çok Yüksek DPI


%prep
%autosetup -p1

# While https://github.com/cassidyjames/dippi/issues/82 is fixed upstream, the
# typo is still present in non-US English localizations—shall we say
# localisations?
sed -r -i 's/(display)‘s/\1’s/g' po/en_*.po

rename_lang() {
  set -ue
  sed -r -i "s/(Language:[[:blank:]]+)${1}\\b/\\1${2}/" \
      "po/${1}.po" "po/extra/${1}.po"
  mv "po/${1}.po" "po/${2}.po"
  mv "po/extra/${1}.po" "po/extra/${2}.po"
  sed -r -i "s/^${1}(\\r?)\$/${2}\\1/" po/LINGUAS po/extra/LINGUAS
}

# https://salsa.debian.org/iso-codes-team/iso-codes/-/blob/v4.16.0/CHANGELOG.md
# See https://bugzilla.redhat.com/show_bug.cgi?id=2279336 for discussion of the
# issue and possible upstreamability.
rename_lang mo ro_MD


%conf
%meson


%build
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
    %{buildroot}/%{_metainfodir}/%{appname}.metainfo.xml
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    %{buildroot}/%{_metainfodir}/%{appname}.metainfo.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_metainfodir}/%{appname}.metainfo.xml


%changelog
%autochangelog
