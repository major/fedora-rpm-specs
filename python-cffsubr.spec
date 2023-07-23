%global srcname cffsubr

Name:           python-%{srcname}
Version:        0.2.9.post1
Release:        8%{?dist}
Summary:        Standalone CFF subroutinizer based on the AFDKO tx tool

# The entire source is Apache-2.0, except:
# - These are derived from fonts licened OFL-1.1, but are not packaged, so they
#   do not contribute to the licenses of the binary RPMs:
#   • tests/data/SourceSansPro-Regular.subset.ttx
#   • tests/data/SourceSansVariable-Regular.subset.ttx
# See NOTICE.
License:        Apache-2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        %{pypi_source %{srcname}}
# Written for Fedora in groff_man(7) format based on the output of “cffsubr --help”
Source1:        %{srcname}.1

BuildArch:      noarch

BuildRequires:  python3-devel
# From setup_requires in setup.py:
BuildRequires:  python3dist(setuptools-scm)

%global txbin /usr/bin/tx

BuildRequires:  %{txbin}
BuildRequires:  symlinks

%description
Standalone CFF subroutinizer based on the AFDKO tx tool.

%generate_buildrequires
%pyproject_buildrequires -x testing

%package -n python3-%{srcname}
Summary:        %{summary}

Requires:       %{txbin}

%description -n python3-%{srcname}
Standalone CFF subroutinizer based on the AFDKO tx tool.

%prep
%autosetup -n %{srcname}-%{version}

# Patch out setuptools-git-ls-files dependency
sed -r -i '/setuptools-git-ls-files/d' setup.py pyproject.toml

# Do not build the extension, which is a copy of the “tx” executable from
# adobe-afdko:
sed -r -i 's/(ext_modules=)/# \1/' setup.py

# Remove bundled adobe-afdko:
rm -rf external

cp -p '%{SOURCE1}' .

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

# Workaround to prevent a dangling symlink:
install -d "%{buildroot}$(dirname '%{txbin}')"
ln -s '%{txbin}' '%{buildroot}%{txbin}'

# Build a relative symbolic link:
ln -s '%{buildroot}%{txbin}' %{buildroot}/%{python3_sitelib}/%{srcname}/tx
symlinks -c -o %{buildroot}/%{python3_sitelib}/%{srcname}/tx

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{srcname}.1'

%check
%if 0%{?fedora} == 33
# Fixing this would require an adobe-afdko update; see
# https://github.com/adobe-type-tools/cffsubr/issues/13.
k="${k-}${k+ and }not (TestSubroutinize and test_non_standard_upem_mute_font_matrix_warning)"
%endif
%pytest -k "${k-}"

%files -n python3-%{srcname} -f %{pyproject_files}
# pyproject-rpm-macros handles the LICENSE file; verify with “rpm -qL -p …”
%doc README.md

# Symbolic link to the “tx” executable; we patched out building a separate copy
# for the Python package, so the Python build does not know about this and we
# must list it explicitly.
%{python3_sitelib}/%{srcname}/tx
# This was just a workaround:
%exclude %{txbin}

%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1*

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.post1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 0.2.9.post1-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.post1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.2.9.post1-5
- Update License to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.post1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.2.9.post1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9.post1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.2.9-1
- Update to 0.2.9 (close RHBZ#2017405)
- Add a man page for the new “cffsubr” CLI entry point

* Tue Oct 26 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.2.8-5
- Drop python3dist(setuptools) BR because it is implied by pyproject-rpm-macros,
  and pyproject-rpm-macros BR because it is (now) implied by python3-devel
- Use the full set of pyproject-rpm-macros

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.8-3
- Rebuilt for Python 3.10

* Mon Mar  1 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.2.8-2
- New upstream version 0.2.8
- Simplify files list
- Patch out (missing) setuptools-git-ls-files BR; add missing setuptool-scm BR
- Unbundle tx executable from adobe-afdko and switch package to noarch
- Drop obsolete python_provide macro
- Use %%pytest macro to run the tests
- Use generated BR’s

* Mon Feb 15 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 0.2.7-1
- Initial packaging
