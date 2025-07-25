# LibreOffice doesn't provide arch-independent extension directory, although
# Grammalecte extension is arch-independant. See also item 6 on
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LibreOfficeExtensions/
%global debug_package %{nil}

%global _description %{expand:Grammalecte is a grammar checker for the French language, derived from
Lightproof. Grammalecte helps writing a proper French, without distracting users
with false positives. This grammar checker follows the principle: the less false
positives, the better; if it cannot know with a good chance that a dubious
expression is wrong, it keeps silent.}
%global _description_fr %{expand:Grammalecte est un correcteur grammatical dédié à la langue française, dérivé de
Lightproof. Grammalecte essaie d'apporter une aide à l'écriture du français sans
parasiter l'attention des utilisateurs avec de fausses alertes. Ce correcteur
suit donc le principe suivant : le moins de « faux positifs » possible ; s'il
n'est pas possible de déterminer avec de fortes chances qu'une suite de mots
douteuse est erronée, le correcteur ne signalera rien.}

Name:           grammalecte
Version:        2.2
Release:        3%{?dist}
Summary:        French grammar checker
Summary(fr):    Correcteur grammatical dédié à la langue française

# Source code is GPL-3.0-only. Language resources in
# gc_lang/fr/oxt/Dictionnaires/dictionaries/ are:
# - MPL-2.0 for dictionaries (*.dic) and affix files (*.aff)
# - LGPL-2.1-or-later for French thesaurus (thes_fr.*) and hyphenation rules (*.tex)
# See ./gc_lang/fr/oxt/Dictionnaires/dictionaries/README*.txt
License:        GPL-3.0-only AND MPL-2.0 AND LGPL-2.1-or-later
URL:            https://grammalecte.net/
Source0:        http://grammalecte.net:8080/tarball/v%{version}/%{name}-%{version}.tar.gz
Source1:        libreoffice-%{name}.metainfo.xml
# Disable failing word suggestion tests due to algorithm change
Patch0:         %{name}-2.2-tests.patch

BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist bottle}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}

%description
%{_description}

%description -l fr
%{_description_fr}


%package -n libreoffice-%{name}
Summary:        French grammar checker for LibreOffice Writer
Summary(fr):    Correcteur grammatical dédié à la langue française pour LibreOffice Writer
Requires:       %{py3_dist grammalecte-fr}
Requires:       libreoffice-langpack-fr
Requires:       libreoffice-pyuno
Requires:       libreoffice-writer

%description -n libreoffice-%{name}
%{_description}

This package provides the LibreOffice Writer extension.

%description -l fr -n libreoffice-%{name}
%{_description_fr}

Ce paquet fournit l'extension pour LibreOffice Writer.


%package -n python3-%{name}
Summary:        French grammar checker
Summary(fr):    Correcteur grammatical dédié à la langue française
Requires:       %{py3_dist bottle}
Provides:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n python3-%{name}
%{_description}

This package provides the command line interface, along with a server and a
Python library.

%description -l fr -n python3-%{name}
%{_description_fr}

Ce paquet fournit l'interface en ligne de commande ainsi qu'un serveur et une
bibliothèque Python.


%prep
%autosetup -p0

# Use system bottle library for build
ln -sf %{python3_sitelib}/bottle.py 3rd/


%build
# Build LibreOffice extension and Python module ZIP
%{python3} make.py -b -d fr

# Build Python module
mkdir python/
unzip _build/Grammalecte-fr-v%{version}.zip -d python/
pushd python/
%pyproject_wheel
popd


%install
# Install LibreOffice extension
install -dm 0755 $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/
unzip _build/Grammalecte-fr-v%{version}.oxt \
    -d $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/ \
    -x "pythonpath/%{name}-cli.py" \
    -x "pythonpath/%{name}/*"
# Fix permissions
find $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/ -type f | xargs chmod 0644

# Install Python module
pushd python/
%pyproject_install
%pyproject_save_files %{name}
popd

# Unbundle bottle library
ln -sf %{python3_sitelib}/bottle.py $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/bottle.py

# Avoid code duplication across subpackages
ln -s %{_bindir}/%{name}-cli.py $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/pythonpath/
ln -s %{python3_sitelib}/%{name} $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/pythonpath/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml


%check
%{py3_test_envvars} %{python3} -m unittest

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml


%files -n libreoffice-%{name}
%doc README.txt
%license LICENSE.txt LICENSE.fr.txt ./gc_lang/fr/oxt/Dictionnaires/dictionaries/README*.txt
%{_libdir}/libreoffice/share/extensions/%{name}/
%{_metainfodir}/%{name}.appdata.xml


%files -n python3-%{name} -f %{pyproject_files}
%doc python/README.txt
%license python/{LICENSE.txt,LICENSE.fr.txt}
%{_bindir}/%{name}-cli.py
%{_bindir}/%{name}-server.py


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2.2-2
- Rebuilt for Python 3.14

* Sat Jan 25 2025 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2-1
- Update to 2.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.2-15
- Fix FTBFS (#RHBZ 2319629)
- Migrate to latest Python packaging guidelines

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.2-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 2.1.2-12
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 2.1.2-8
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.2-5
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.2-2
- Rebuilt for Python 3.10

* Sun Mar 21 2021 Mohamed El Morabity - 2.1.2-1
- Update to 2.1.2

* Thu Feb 25 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Mon Feb 15 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sat Nov 28 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.12.2-3
- Fix Python >= 3.10 detection

* Tue Oct 06 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.12.2-2
- Add BuildRequires on python3-setuptools

* Wed Sep 02 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.12.2-1
- Initial RPM release
