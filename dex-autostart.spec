Name:           dex-autostart
Version:        0.9.0
Release:        6%{?dist}
Summary:        Generate and execute DesktopEntry files

License:        GPLv3+
URL:            https://github.com/jceb/dex
Source0:        https://github.com/jceb/dex/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz


BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires: make
BuildArch:      noarch

%description
dex-autostart, DesktopEntry Execution, is a program to generate and execute
DesktopEntry files of the Application type.


%prep
%autosetup -n dex-%{version}


%build
%make_build VERSION=%{version}

# fix name in man page
sed -i "s/dex/dex-autostart/g" dex.1
sed -i "s/DEX/DEX-AUTOSTART/g" dex.1

# fix name in README
sed -i "s/dex/dex-autostart/g" README.rst
sed -i "s/DEX/DEX-AUTOSTART/g" README.rst



%install
%make_install PREFIX=/usr MANPREFIX=%{_mandir} NAME=%{name} VERSION=%{version}

# do not install the license twice
rm %{buildroot}/%{_defaultdocdir}/%{name}/LICENSE


%check
%{buildroot}/%{_bindir}/%{name} --test -v



%files
%license LICENSE
%{_defaultdocdir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}



%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Till Hofmann <thofmann@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.7

* Wed May 30 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.8.0-1
- Update to released version 0.8.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.12.20150728git4bbd9f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8-0.11.20150728git4bbd9f9
- Build docs with Python 3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.10.20150728git4bbd9f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.9.20150728git4bbd9f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8-0.8.20150728git4bbd9f9
- Rebuild for Python 3.6

* Thu Aug 04 2016 Till Hofmann <till.hofmann@posteo.de> - 0.8-0.7.20150728git4bbd9f9
- Add patch to build the manpage in a separate build dir (fixes FTBFS)
- Set version build variable to avoid calling git during the build process
- Add name substitution for capitalized name: DEX->DEX-AUTOSTART

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-0.6.20150728git4bbd9f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.5.20150728git4bbd9f9
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jul 28 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8-0.4.20150728git4bbd9f9
- Update to new upstream 4bbd9f9 (patch included upstream)
- Properly rename dex -> dex-autostart in README
- Add check section

* Sun Jul 26 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8-0.3.20150714gita98fa2f
- Fix name in man page

* Sun Jul 12 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8-0.2.20150714gita98fa2f
- Remove LICENSE from docdir

* Sun Jul 12 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.8-0.1.20150714gita98fa2f
- Initial package
