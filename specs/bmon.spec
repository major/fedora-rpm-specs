Name:           bmon
Version:        4.0
Release:        12%{?dist}
Summary:        Bandwidth monitor and rate estimator

License:        BSD-2-Clause and MIT
URL:            https://github.com/tgraf/bmon
Source0:        https://github.com/tgraf/bmon/releases/download/v%{version}/bmon-%{version}.tar.gz

Patch1:         bmon-4.0-buffer_size.patch

BuildRequires:  gcc
BuildRequires:  libconfuse-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
bmon is a monitoring and debugging tool to capture networking related
statistics and prepare them visually in a human friendly way. It
features various output methods including an interactive curses user
interface and a programmable text output for scripting.

%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

%files
%license LICENSE.BSD
%license LICENSE.MIT
%{_bindir}/bmon
%{_mandir}/man8/bmon.8*
%{_docdir}/bmon/examples/bmon.conf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 14 2023 Boian Bonev <bbonev@ipacct.com> - 4.0-7
- SPDX migration, correct license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Boian Bonev <bbonev@ipacct.com> - 4.0-1
- Update to 4.0 release
- Add a trivial patch for possible snprintf string truncation

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.7-8
- libconfuse rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.7-5
- libconfuse rebuild.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Jon Ciesla <limburgher@gmail.com> - 3.7-3
- libconfuse rebuild.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.7-1
- Update to 3.7 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Thomas Graf <tgraf@suug.ch> - 3.6-1
- Update to 3.6 release

* Sat Aug 30 2014 Thomas Graf <tgraf@suug.ch> - 3.5-1
- Update to 3.5 release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 15 2013 Thomas Graf <tgraf@suug.ch> - 3.1-4
- Use install -p to preserve timestamp of non generated files

* Sun Sep 15 2013 Thomas Graf <tgraf@suug.ch> - 3.1-3
- Declare GPL license usage due to list.h
- Use version macro in spec file
- Enable verbose building via V=1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Thomas Graf <tgraf@suug.ch> - 3.1-1
- Initial release
