%global module_name bmaptools

Name:           bmap-tools
Version:        3.6
Release:        8%{?dist}
Summary:        Tools to generate and flash sparse images using the "block map" (bmap) format
License:        GPLv2+
URL:            https://github.com/intel/bmap-tools
Source0:        https://github.com/intel/bmap-tools/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# Base package contains the command line tool, which uses the Python library
Requires:       python3-%{module_name} = %{version}-%{release}

%description
Bmaptool is a generic tool for creating the block map (bmap) for a file and 
copying files using the block map. The idea is that large files, like raw 
system image files, can be copied or flashed a lot faster and more reliably 
with bmaptool than with traditional tools, like dd or cp.

Bmaptool was originally created for the "Tizen IVI" project and it was used for
flashing system images to USB sticks and other block devices. Bmaptool can also
be used for general image flashing purposes, for example, flashing Fedora Linux
OS distribution images to USB sticks.

%package -n python3-%{module_name}
Summary:        Python library for bmap-tools
%{?python_provide:%python_provide python3-%{module_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
Requires:       python3-six
Requires:       python3-gpg
Requires:       bzip2
Requires:       pbzip2
Requires:       gzip
Requires:       xz
Requires:       tar
Requires:       unzip
Requires:       lzop
Requires:       pigz
Requires:       zstd

%description -n python3-%{module_name}
Python library to manipulate sparse images in the "block map" (bmap) format.

%prep
%setup -q
# Remove unnecessary shebang
sed -i -e '/^#!/,1d' bmaptools/CLI.py

%build
%py3_build

%install
%py3_install
install -d %{buildroot}/%{_mandir}/man1
install -m644 docs/man1/bmaptool.1 %{buildroot}/%{_mandir}/man1

%files
%{_bindir}/bmaptool
%{_mandir}/man1/bmaptool.1*

%files -n python3-%{module_name}
%doc docs/README docs/RELEASE_NOTES
%license COPYING
%{python3_sitelib}/%{module_name}
%{python3_sitelib}/bmap_tools*.egg-info

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.6-8
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.6-5
- Rebuilt for Python 3.11

* Tue Mar 15 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.6-4
- Missing zstd dependency added

* Tue Mar 15 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.6-3
- Deprecated build dependency python3-nose removed

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 08 2021 Dan Callaghan <djc@djc.id.au> - 3.6-1
- new upstream release 3.6 (RHBZ#1978386)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.5-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5-3
- Rebuilt for Python 3.9

* Mon Dec 30 2019 Dan Callaghan <dan.callaghan@opengear.com> - 3.5-2
- dropped the separate 'bmaptool' subpackage, the base package now provides
  /usr/bin/bmaptool

* Tue Jan 29 2019 Dan Callaghan <dan.callaghan@opengear.com> - 3.5-1
- initial version
