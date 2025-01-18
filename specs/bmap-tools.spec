%global module_name bmaptools

Name:           bmap-tools
Version:        3.7
Release:        7%{?dist}
Summary:        Tools to generate and flash sparse images using the "block map" (bmap) format

License:        GPL-2.0-or-later
URL:            https://github.com/intel/bmap-tools
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  gnupg2
Requires:       bzip2
Requires:       pbzip2
Requires:       gzip
Requires:       xz
Requires:       tar
Requires:       unzip
Requires:       lzop
Requires:       pigz
Requires:       zstd

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

%description -n python3-%{module_name}
Python library to manipulate sparse images in the "block map" (bmap) format.

%prep
%autosetup
# Remove unnecessary shebang
sed -i -e '/^#!/,1d' bmaptools/CLI.py
sed -i -e '/^#!/,1d' bmaptools/__main__.py

# https://github.com/yoctoproject/bmaptool/pull/1#issuecomment-1986205242
export GNUPGHOME=$PWD/tests/test-data/gnupg
echo 'expire
50y
key 1
expire
50y
save' | gpg --command-fd=0 --batch --edit-key 927FF9746434704C5774BE648D49DFB1163BDFB4

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module_name}

install -d %{buildroot}/%{_mandir}/man1
install -m644 docs/man1/bmaptool.1 %{buildroot}/%{_mandir}/man1

%check
%pytest -v

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/bmaptool
%{_mandir}/man1/bmaptool.1*

%files -n python3-%{module_name} -f %{pyproject_files}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.7-6
- Resolves: rhbz#2300579

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.7-4
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 11 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 3.7-1
- Update to 3.7

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
