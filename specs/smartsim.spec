#global git_date 20120830
#global git_hash 3b11cf8

Name:           smartsim
URL:            http://smartsim.org.uk/
Version:        1.4
Release:        25%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
Summary:        Digital logic circuit design and simulation package
Source0:        https://github.com/ashleynewson/SmartSim/archive/v1.4.tar.gz
#Source0:        https://github.com/ashleynewson/SmartSim/tarball/%{git_hash}/smartsim-%{git_hash}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk3-devel libxml2-devel librsvg2-devel
BuildRequires:  ImageMagick desktop-file-utils

%description
SmartSim is a free and open source digital logic circuit design and
simulation package.

SmartSim lets you create complex circuits by allowing you to create
your own custom components and including them in other circuits, as if
they were any other built-in component. These larger circuits can then
also be included in other designs as sub-components. SmartSim also
offers the ability to print out or export your circuit designs to PDF,
PNG, or SVG.

When you have finished designing your circuit, SmartSim offers an
interactive simulation feature, allowing you to control your circuit
and explore inside sub-components whilst the circuit is
running. SmartSim also allows you to produce logic timing diagrams
from your simulation's activity, which can then be exported to PDF,
PNG, and SVG formats.

%prep
%setup -q -n SmartSim-%{version}
#setup -q -n ashleynewson-SmartSim-%{git_hash}
./configure --prefix=%{_prefix} --libdir=%{_libdir}

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

# create desktop file
cat <<EOF >smartsim.desktop
[Desktop Entry]
Name=smartsim
GenericName=SmartSim
Exec=smartsim
Icon=smartsim
Terminal=false
Type=Application
Categories=Engineering;
EOF

%install
make install DESTDIR="%{buildroot}"

install -d -m 755 %{buildroot}%{_datadir}/applications
install -p -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications

install -d -m 755 %{buildroot}%{_datadir}/pixmaps
convert %{buildroot}%{_datadir}/%{name}/%{name}.ico  %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc COPYING README
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4-24
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Eric Smith <spacewar@gmail.com> 1.4-1
- Update to latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 04 2012 Eric Smith <spacewar@gmail.com> 1.2.1-1
- initial version
