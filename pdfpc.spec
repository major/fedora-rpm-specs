Name:           pdfpc
Version:        4.5.0
Release:        8%{?dist}
Summary:        A GTK based presentation viewer application for GNU/Linux

License:        GPLv2+
URL:            https://%{name}.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gtk3-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  json-glib-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libgee-devel
BuildRequires:  pango-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  webkit2gtk3-devel
BuildRequires:  vala vala-devel

%description
pdfpc is a GTK based presentation viewer application for GNU/Linux which uses
Keynote like multi-monitor output to provide meta information to the speaker
during the presentation. It is able to show a normal presentation window on one
screen, while showing a more sophisticated overview on the other one providing
information like a picture of the next slide, as well as the left over time
till the end of the presentation. The input files processed by pdfpc are PDF
documents, which can be created using nearly any of today's presentation
software.

%prep
%autosetup -n %{name}-%{version} -S git


%build
%cmake -DSYSCONFDIR=/etc .
%cmake_build


%install
%cmake_install


%files
%doc README.rst CHANGELOG.rst
%{_bindir}/%{name}
%license LICENSE.txt
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*
%{_datadir}/pixmaps/%{name}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.5.0-6
- Rebuld for vala update, should fix FTBFS

* Thu Jul 29 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.5.0-5
- Rebuild for poppler update

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.5.0-2
- Rebuild for poppler 21.01.0

* Sun Jan 10 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.5.0-1
- Update to latest release

* Wed Sep 30 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.4.0-4
- Use cmake macros to fix build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.4.0-1
- Update to latest release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 4.3.4-4
- Rebuild for poppler-0.84.0

* Sun Aug 04 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.3.4-3
- Add patch to fix FTBFS
- https://bugzilla.redhat.com/show_bug.cgi?id=1736412
- https://github.com/pdfpc/pdfpc/pull/446

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.3.4-1
- Update to new version

* Sun Feb 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.3.2-1
- Update to latest upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.3.1-1
- Update to latest release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.1.2-1
- Update to latest release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Michael J Gruber <mjg@fedoraproject.org> - 4.1-1
- clean up source and setup
- Update to 4.1

* Sat Aug 26 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.0.8-1
- Update to 4.0.8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.0.7-1
- Update to new release

* Wed Feb 22 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.0.6-1
- Update to latest upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 4.0.1-4
- another specfile fix

* Thu Jan 07 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 4.0.1-3
- specfile fix

* Thu Jan 07 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 4.0.1-2
- Fix sourceurl to fix build

* Thu Jan 07 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 4.0.1-1
- update to latest upstream release

* Sat Jun 20 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 4.0.0-2
- Had forgotten license
- https://bugzilla.redhat.com/show_bug.cgi?id=1232273#c1

* Mon Jun 15 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 4.0.0-1
- New version

* Mon Jun 15 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 3.1.1-1
- Initial rpm build
