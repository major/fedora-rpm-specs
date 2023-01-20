Name:           xnec2c
Version:        4.1.1
Release:        6%{?dist}
Summary:        GTK based graphical wrapper for nec2c

License:        GPLv2+
URL:            http://www.5b4az.org/
Source0:        http://www.5b4az.org/pkg/nec2/xnec2c/%{name}-%{version}.tar.bz2
Source100:      xnec2c.png
Patch0: xnec2c-configure-c99.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  make

Requires:       nec2c%{?_isa}

%description
xnec2c is a GUI interactive application that (in its current form) reads NEC2
input files but presents output data in graphical form, e.g. as wire frame
drawings of the radiation pattern or near E/H field, graphs of maximum gain,
input impedance, vswr etc against frequency and simple rendering of the antenna
structure, including color code representation of currents or charge densities.

These results are only calculated and drawn on user demand via menu items or
buttons, e.g. xnec2c is interactive and does not execute NEC2 "commands" in
batch style as the original does. 


%prep
%autosetup -p1
%if 0%{?rhel}
    # Force lower version of intltool to be acceptable for RHEL.
    sed -i "s|0.50.0|0.40.0|g" configure
%endif


pushd examples
iconv --from=ISO-8859-1 --to=UTF-8 conductivity.txt > conductivity.txt.new && \
touch -r conductivity.txt conductivity.txt.new && \
mv conductivity.txt.new conductivity.txt


%build
%configure
%make_build CFLAGS="%{optflags}"


%install
%make_install

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -pm 644 %{SOURCE100} \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
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
  <summary>GTK based graphical wrapper for nec2c</summary>
  <description>
    <p>
nec2c is a GUI interactive application that (in its current form) reads NEC2
input files but presents output data in graphical form, e.g. as wire frame
drawings of the radiation pattern or near E/H field, graphs of maximum gain,
input impedance, vswr etc against frequency and simple rendering of the antenna
structure, including color code representation of currents or charge densities.
    </p>
  </description>
  <screenshots>
    <screenshot type="default">
      <image>http://www.5b4az.org/pkg/nec2/xnec2c/doc/images/radiation.png</image>
    </screenshot>
  </screenshots>
  <url type="homepage">%{url}</url>
  <update_contact>hobbes1069@gmail.com</update_contact>
</component>
EOF
%endif


%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
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
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{?fedora:%{_datadir}/appdata/%{name}.appdata.xml}
%{_mandir}/man1/%{name}.*


%changelog
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
