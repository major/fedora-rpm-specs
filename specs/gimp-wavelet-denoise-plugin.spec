Name:           gimp-wavelet-denoise-plugin
Version:        0.4
Release:        3%{?dist}
Summary:        Gimp wavelet denoise plugin

License:        GPL-2.0-or-later
URL:            https://github.com/mrossini-ethz/gimp-wavelet-denoise
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
#Patch0:         gimp-wavelet-denoise-plugin-fno-common-fix.patch

BuildRequires:  gcc
BuildRequires:  gimp-devel >= 2.4.0
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  make

Requires:       gimp >= 2.4

%description
The wavelet denoise plugin is a tool to reduce noise in each channel of an
image separately. The default colour space to do denoising is YCbCr which
has the advantage that chroma noise can be reduced without affecting image
details. Denoising in CIELAB (L*a*b*) or RGB is available as an option.
The user interface allows colour mode and preview channel selection.
The denoising threshold can be set for each colour channel independently.

%prep
%autosetup -p1 -n gimp-wavelet-denoise-%{version}
sed -i -e 's/CFLAGS.*/& $(shell echo $$CFLAGS)/' src/Makefile
sed -i -e "s!    59 Temple Place, Suite 330, Boston, MA  02111-1307  USA!51\ Franklin Street,\ Fifth\ Floor,\ Boston,\ MA!" COPYING


%build
%set_build_flags
%make_build


%install
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
sed -i "s|/usr/share/locale|%{buildroot}%{_datadir}/locale|" po/Makefile
mkdir -p %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
install -m 0755 -p src/wavelet-denoise %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
mkdir -p %{buildroot}%{_datadir}/locale/de/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/it/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/et/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES
make install po
%find_lang gimp20-wavelet-denoise-plug-in


%files -f gimp20-wavelet-denoise-plug-in.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/gimp/2.0/plug-ins/wavelet-denoise


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.0-1
- Update to 0.4.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.1-9
- Correct FSF address

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1-4
- Correct exec bits for plugin

* Wed Apr 23 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1-3
- Correct install parameters

* Mon Mar 31 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1-2
- Correct CFLAGS

* Tue May 15 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1-1
- initial release
