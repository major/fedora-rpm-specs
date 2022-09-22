Name:           ladspa-autotalent-plugins
Version:        0.2
Release:        26%{?dist}
Summary:        A pitch correction LADSPA plugin

# The files mayer_fft.h and mayer_hht.c are from Pure Data, which is under a
# standard improved BSD license.  autotalent.c is under GPLv2+.
License:        GPLv2+ and BSD and CC-BY-ND
URL:            http://web.mit.edu/tbaran/www/autotalent.html
Source0:        http://web.mit.edu/tbaran/www/autotalent-%{version}.tar.gz
# Useful documentation is not included in the upstream source distribution.
Source1:        http://web.mit.edu/tbaran/www/autotalent-%{version}_refcard.pdf

BuildRequires:  gcc
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa

%description
Autotalent is a real-time pitch correction plugin. You specify the notes that
a singer is allowed to hit, and Autotalent makes sure that they do. You can
also use Autotalent for more exotic effects, making your voice sound like a
chiptune, adding artificial vibrato, or messing with your formants.
Autotalent can also be used as a harmonizer that knows how to sing in the
scale with you. Or, you can use Autotalent to change the scale of a melody
between major and minor or to change the musical mode. 

%prep
%setup -q -n autotalent-%{version}
cp %{SOURCE1} .

# Use the correct Fedora optimization flags
sed -i 's|-O3|%{optflags}|' Makefile

# Use the system ladspa.h
rm ladspa.h
sed -i 's|"ladspa.h"|<ladspa.h>|' autotalent.c
sed -i 's|ladspa.h||' Makefile


%build
make %{?_smp_mflags} LDFLAGS="$RPM_LD_FLAGS -nostartfiles -shared -Wl,-Bsymbolic -lc -lm -lrt"


%install
make install INSTALL_PLUGINS_DIR="%{buildroot}%{_libdir}/ladspa"



%files
%doc README
%license COPYING COPYING-mayer_fft
%doc autotalent-0.2_refcard.pdf
%{_libdir}/ladspa/*



%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.2-17
- Use Fedora link flags
- Add BR: gcc
- Some cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 28 2010 David Cornette <rpm@davidcornette.com> 0.2-3
- Updated to upstream package which includes the license file for the Pure Data
  source files

* Sun May 23 2010 David Cornette <rpm@davidcornette.com> 0.2-2
- Changed License: field to reflect license of the reference card pdf

* Fri May 14 2010 David Cornette <rpm@davidcornette.com> 0.2-1
- Initial build

