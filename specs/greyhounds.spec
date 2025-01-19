Name:           greyhounds
Version:        0.8
Release:        0.44.prealpha%{?dist}
Summary:        Greyhounds is a greyhounds racing and breeding game
Summary(pl):    Greyhounds to wyścigi i hodowla chartów
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://sourceforge.net/projects/byghound
Source0:        http://downloads.sourceforge.net/byghound/%{name}-%{version}-pre-alpha.tar.bz2
Source1:        %{name}.desktop
# Patch 0 should go upstrem
Patch0:		greyhound-am.patch
Patch1:		greyhound-in.patch
Patch2:		greyhound-save.patch
Patch3:		greyhound-gcc10.patch
Patch4:		greyhound-names.patch
Patch5:		greyhounds-configure-c99.patch
Patch6:		greyhounds-c99-headers.patch
BuildRequires:  gcc
BuildRequires:  desktop-file-utils gtk2-devel ImageMagick
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Greyhounds is a greyhound racing and breeding game. Your goal is to
acquire fast and talented greyhounds and be successful with them in the
races; your two possibilities for doing so are breeding and trading.
Ultimately you should aim at winning the Champions' Trophy. You might
also consider establishing a record that lasts to the end of times a
worthy goal.

%description -l pl
Greyhounds to wyścigi i hodowla chartów. Twoim zadaniem jest zdobyć szybkie
i utalentowane charty i być zadowolonym z ich wyścigów; twoimi dwiema
możliwościami są hodowanie i handlowanie. Ostatecznie powinineś dążyć do
wygraia mistrzowskiego trofeum. Możesz również osiągać nowe rekordy
czasowe.

%prep
%setup -q -n %{name}-%{version}-pre-alpha
%patch -P0
%patch -P1
%patch -P2
%patch -P3
%patch -P4
%patch -P5 -p1
%patch -P6 -p1

# Create icons and make appropriate dir structure
mkdir icons
for size in 16 22 24 32 36 48; do
  mkdir -p icons/${size}x${size}/apps
  convert pixmaps/logo.xpm -resize ${size}x${size} icons/${size}x${size}/apps/%{name}.png
done

# Convert doc to UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 README > README.utf8
mv README.utf8 README

iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.utf8
mv AUTHORS.utf8 AUTHORS

%build

%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor
cp -pr icons/*x* $RPM_BUILD_ROOT%{_datadir}/icons/hicolor

# Desktop file
desktop-file-install                                    \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE1}

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.44.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8-0.43.prealpha
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.42.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.41.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.40.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.39.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.38.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Florian Weimer <fweimer@redhat.com> - 0.8-0.37.prealpha
- Apply fixes to build with C99 compilers

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.36.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.35.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.34.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.33.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.32.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 09 2020 Bruno Wolff III <bruno@wolff.to> - 0.8-0.31.prealpha
- Array names was declared the wrong size

* Sat Feb 08 2020 Bruno Wolff III <bruno@wolff.to> - 0.8-0.30.prealpha
- Fix duplicate definition detected by gcc 10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.29.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.28.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.27.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.26.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.25.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8-0.24.prealpha
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.23.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.22.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.21.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.20.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.19.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.18.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.17.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.16.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> - 0.8-0.15.prealpha
- Remove vendor prefix from desktop file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.14.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.13.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.12.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Bruno Wolff III <bruno@wolff.to> - 0.8-0.11.prealpha
- Rebuild for libpng 1.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.10.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Mar 27 2010 Bruno Wolff III <bruno@wolff.to> - 0.8-0.9.prealpha
* Add a desktop subcategory under games (simulation) - Bug 485351

* Sat Mar 27 2010 Bruno Wolff III <bruno@wolff.to> - 0.8-0.8.prealpha
- Another possible fix for save game issue - Bug 562038

* Sat Mar 27 2010 Bruno Wolff III <bruno@wolff.to> - 0.8-0.7.prealpha
- Possible fix for save game issue - Bug 562038

* Fri Mar 26 2010 Bruno Wolff III <bruno@wolff.to> - 0.8-0.6.prealpha
- Include -lm to fix DSO issue - Bug 565040

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.5.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.4.prealpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 16 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 0.8-0.3.prealpha
- Correct license

* Sat Feb 16 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 0.8-0.3.prealpha
- Correct license
- Correct Source0

* Wed Feb 13 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 0.8-0.1.prealpha
- First release
