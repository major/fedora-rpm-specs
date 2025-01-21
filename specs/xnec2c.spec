Name:           xnec2c
Version:        4.4.16
Release:        5%{?dist}
Summary:        GTK based graphical wrapper for nec2c

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/
Source0:        https://github.com/KJ7LNW/xnec2c/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source100:      xnec2c.png

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make

Requires:       nec2c%{?_isa}
# For BLAS acceleration.  Really these are suggested, but strongly
# recommended for performance.  xnec2c detects available BLAS
# libraries at runtime:
Recommends: atlas
Recommends: openblas-serial
Recommends: openblas-threads
Recommends: openblas-openmp


%description
Xnec2c is a high-performance multi-threaded electromagnetic simulation
package to model antenna near- and far-field radiation patterns for
Linux and UNIX operating systems. The original FORTRAN version of NEC2
was ported to C by Neoklis Kyriazis, 5B4AZ and released as nec2c. Later
he wrote xnec2c, a graphical interface for ease of use with many more
features:
	Multi-threading operation on SMP machines
	On-demand Calculation
	Built-in NEC2 input file editor
	Accelerated Linear Algebra Support
	Interactive Operation
	User Interface
	Color Coding
	and much more.


%prep
%autosetup -p1

pushd examples
iconv --from=ISO-8859-1 --to=UTF-8 conductivity.txt > conductivity.txt.new && \
touch -r conductivity.txt conductivity.txt.new && \
mv conductivity.txt.new conductivity.txt


%build
autoreconf -fi
%configure
%make_build CFLAGS="%{optflags}"


%install
%make_install

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -pm 644 %{SOURCE100} \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

# Install scalable icon for Fedora
# Note /usr/share/pixmap/xnec2c.svg is needed for the icon to show in el7.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -pm 644 resources/xnec2c.svg \
	%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

desktop-file-install --vendor="" \
  --dir=%{buildroot}%{_datadir}/applications \
  files/%{name}.desktop

# Remove incorrectly installed files by make
rm -rf %{buildroot}%{_docdir}/%{name}/*.1.gz \
       %{buildroot}%{_datadir}/pixmaps

%if 0%{?fedora}
# Appdata
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2017 Richard Shaw <hobbes1069@gmail.com> -->
<component type="desktop">
  <id>%{name}.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-2.0+</project_license>
  <name>xnec2c</name>
  <summary>A multi-threaded EM tool based on NEC2 to model antenna radiation patterns.</summary>
  <description>
    <p>
Xnec2c is a high-performance multi-threaded electromagnetic simulation
package to model antenna near- and far-field radiation patterns for
Linux and UNIX operating systems. The original FORTRAN version of NEC2
was ported to C by Neoklis Kyriazis, 5B4AZ and released as nec2c. Later
he wrote xnec2c, a graphical interface for ease of use with many more
features.
    </p>
  </description>
  <categories>
  	<category>Electronics</category>
  	<category>Science</category>
  	<category>Math</category>
  	<category>NumericalAnalysis</category>
  </categories>
  <screenshots>
    <screenshot type="default">
      <image>https://www.xnec2c.org/images/radiation.png</image>
    </screenshot>
  </screenshots>
  <url type="homepage">%{url}</url>
  <content_rating type="oars-1.1"/>
  <update_contact>hobbes1069@gmail.com</update_contact>
</component>
EOF
%endif


%files
%doc AUTHORS ChangeLog README
%doc doc/NearFieldCalcs.txt doc/NEC2-bug.txt doc/nec2c.txt doc/xnec2c.html
%doc doc/images
%doc examples
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/x-nec2.xml
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{?fedora:%{_datadir}/appdata/%{name}.appdata.xml}
%{_mandir}/man1/%{name}.*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.4.16-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 4.4.16-2
- Soften atlas dependency

* Sun Jun 02 2024 Richard Shaw <hobbes1069@gmail.com> - 4.4.16-1
- Update to 4.4.16.

* Sat Apr 06 2024 Richard Shaw <hobbes1069@gmail.com> - 4.4.13-1
- Update to 4.4.13.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Florian Weimer <fweimer@redhat.com> - 4.1.1-6
- Port configure script to C99 (#2161646)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.1-1
- Update to 4.1.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Richard Shaw <hobbes1069@gmail.com> - 3.9-0.1
- Update to 3.9 Beta with GTK3 suppoert.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 04 2017 Richard Shaw <hobbes1069@gmail.com> - 3.5.1-1
- Update to latest upstream release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Richard Shaw <hobbes1069@gmail.com> - 3.3-1
- Update to latest upstream release.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Richard Shaw <hobbes1069@gmail.com> - 2.8-1
- Update to latest upstream release.

* Mon Aug 26 2013 Richard Shaw <hobbes1069@gmail.com> - 2.3-1.beta
- Update to latest upstream release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 03 2013 Richard Shaw <hobbes1069@gmail.com> - 2.1-1.beta
- Update to latest upstream release.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
