Name:       mathjax
Version:    2.7.4
Release:    %autorelease
Summary:    JavaScript library to render math in the browser
License:    Apache-2.0
URL:        http://mathjax.org
Source0:    https://github.com/mathjax/MathJax/archive/%{version}.tar.gz#/mathjax-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:   web-assets-devel
BuildRequires:   fontpackages-devel

Requires:        web-assets-filesystem
Requires:        %{name}-ams-fonts
Requires:        %{name}-caligraphic-fonts
Requires:        %{name}-fraktur-fonts %{name}-main-fonts
Requires:        %{name}-math-fonts
Requires:        %{name}-sansserif-fonts
Requires:        %{name}-script-fonts
Requires:        %{name}-typewriter-fonts
Requires:        %{name}-size1-fonts
Requires:        %{name}-size2-fonts
Requires:        %{name}-size3-fonts
Requires:        %{name}-size4-fonts
Requires:        %{name}-size1-fonts
Requires:        %{name}-winie6-fonts
Requires:        %{name}-winchrome-fonts
Requires:        %{name}-vector-fonts
Requires:        %{name}-stixweb-fonts

%description
MathJax is an open-source JavaScript display engine for LaTeX, MathML,
and AsciiMath notation that works in all modern browsers. It requires no
setup on the part of the user (no plugins to download or software to
install), so the page author can write web documents that include
mathematics and be confident that users will be able to view it
naturally and easily. Supports LaTeX, MathML, and AsciiMath notation
in HTML pages.

%global fontsummary Fonts used by MathJax to display math in the browser

%package       ams-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   ams-fonts
%{fontsummary}.

%package       caligraphic-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   caligraphic-fonts
%{fontsummary}.

%package       fraktur-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   fraktur-fonts
%{fontsummary}.

%package       main-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   main-fonts
%{fontsummary}.

%package       math-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   math-fonts
%{fontsummary}.

%package       sansserif-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   sansserif-fonts
%{fontsummary}.

%package       script-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   script-fonts
%{fontsummary}.

%package       typewriter-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   typewriter-fonts
%{fontsummary}.

%package       size1-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   size1-fonts
%{fontsummary}.

%package       size2-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   size2-fonts
%{fontsummary}.

%package       size3-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   size3-fonts
%{fontsummary}.

%package       size4-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   size4-fonts
%{fontsummary}.

%package       winie6-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   winie6-fonts
%{fontsummary}.

%package       winchrome-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   winchrome-fonts
%{fontsummary}.

%package       vector-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   vector-fonts
%{fontsummary}.

%package       stixweb-fonts
Summary:       %{fontsummary}
Requires:      fontpackages-filesystem
License:       OFL-1.1
%description   stixweb-fonts
%{fontsummary}.

%prep
%setup -q -n MathJax-%{version}
# Remove bundled fonts
rm -rf MathJax-%{version}/jax/output
rm -rf MathJax-%{version}/fonts/HTML-CSS/{Asana-Math,Gyre-Pagella,Gyre-Termes,Latin-Modern,Neo-Euler}

# Remove minified javascript.
for i in $(find . -type f -path '*unpacked*'); do \
  mv $i ${i//unpacked/}; done
find . -depth -type d -path '*unpacked*' -delete
for i in MathJax.js jax/output/HTML-CSS/jax.js jax/output/HTML-CSS/imageFonts.js; do \
    sed -r 's#(MathJax|BASE)[.]isPacked#1#' <$i >$i.tmp; \
    touch -r $i $i.tmp; \
    mv $i.tmp $i; \
done

# Remove .htaccess file, just in case
find . -name .htaccess -print -delete

%build
# minification should be performed here at some point

%install
mkdir -p %{buildroot}%{_jsdir}/mathjax
cp -pr MathJax.js config/ extensions/ jax/ localization/ test/ \
    %{buildroot}%{_jsdir}/mathjax/

mkdir -p %{buildroot}%{_fontdir}

# TeX fonts
mkdir -p %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/TeX/
cp -pr fonts/HTML-CSS/TeX/png %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/TeX/

cp -pr fonts/HTML-CSS/TeX/*/MathJax_*.{eot,otf,svg} %{buildroot}%{_fontdir}

for t in eot otf svg; do \
    mkdir -p %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/TeX/$t; \
    for i in fonts/HTML-CSS/TeX/$t/MathJax_*.$t; do \
        ln -s %{_fontdir}/$(basename $i) \
            %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/TeX/$t/; \
    done \
done

# STIX-Web fonts
mkdir -p %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/STIX-Web/
cp -pr fonts/HTML-CSS/STIX-Web/*/STIXMathJax_*.{eot,otf} %{buildroot}%{_fontdir}

for t in eot otf; do \
    mkdir -p %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/STIX-Web/$t; \
    for i in fonts/HTML-CSS/STIX-Web/$t/STIXMathJax_*.$t; do \
        ln -s %{_fontdir}/$(basename $i) \
            %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/STIX-Web/$t/; \
    done \
done

%files
%{_jsdir}/mathjax
%doc README.md LICENSE

%_font_pkg -n %{name}-AMS MathJax_AMS*.eot MathJax_AMS*.otf MathJax_AMS*.svg
%_font_pkg -n %{name}-Caligraphic MathJax_Caligraphic*.eot MathJax_Caligraphic*.otf MathJax_Caligraphic*.svg
%_font_pkg -n %{name}-Fraktur MathJax_Fraktur*.eot MathJax_Fraktur*.otf MathJax_Fraktur*.svg
%_font_pkg -n %{name}-Main MathJax_Main*.eot MathJax_Main*.otf MathJax_Main*.svg
%_font_pkg -n %{name}-Math MathJax_Math*.eot MathJax_Math*.otf MathJax_Math*.svg
%_font_pkg -n %{name}-SansSerif MathJax_SansSerif*.eot MathJax_SansSerif*.otf MathJax_SansSerif*.svg
%_font_pkg -n %{name}-Script MathJax_Script*.eot MathJax_Script*.otf MathJax_Script*.svg
%_font_pkg -n %{name}-Typewriter MathJax_Typewriter*.eot MathJax_Typewriter*.otf MathJax_Typewriter*.svg
%_font_pkg -n %{name}-Size1 MathJax_Size1*.eot MathJax_Size1*.otf MathJax_Size1*.svg
%_font_pkg -n %{name}-Size2 MathJax_Size2*.eot MathJax_Size2*.otf MathJax_Size2*.svg
%_font_pkg -n %{name}-Size3 MathJax_Size3*.eot MathJax_Size3*.otf MathJax_Size3*.svg
%_font_pkg -n %{name}-Size4 MathJax_Size4*.eot MathJax_Size4*.otf MathJax_Size4*.svg
%_font_pkg -n %{name}-WinIE6 MathJax_WinIE6*.eot MathJax_WinIE6*.otf
%_font_pkg -n %{name}-WinChrome MathJax_WinChrome*.otf MathJax_WinChrome*.svg
%_font_pkg -n %{name}-Vector MathJax_Vector*.eot MathJax_Vector*.otf MathJax_WinChrome*.svg
%_font_pkg -n %{name}-STIXWeb STIXMathJax_*.eot STIXMathJax_*.otf

%changelog
%autochangelog
