%global         srcname         svg2tikz
%global         forgeurl        https://github.com/xyz2tex/svg2tikz
Version:        3.2.0
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        3%{?dist}
Summary:        Convert SVG to TikZ/PGF code

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}


BuildRequires:  python3-devel
BuildRequires:  gobject-introspection-devel
Requires:       xclip

BuildArch: noarch

%global _description %{expand:
SVG2TikZ, formally known as Inkscape2TikZ, are a set of tools for
converting SVG graphics to TikZ/PGF code.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%package -n inkscape-%{srcname}
Summary:        Inkscape svg2tikz extension
Requires:       python3-%{srcname}
Requires:       inkscape

%description -n inkscape-%{srcname} %_description


%prep
%forgeautosetup

#Remove version limit from lxml
sed -i "s/lxml =.*/lxml = '\*'/" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}
# Executable fix
chmod -x %{buildroot}%{python3_sitelib}/%{srcname}/__init__.py
# Shebang fix
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{srcname}/tikz_export.py
chmod +x %{buildroot}%{python3_sitelib}/%{srcname}/tikz_export.py
	
 
# Inkscape-extension
mkdir -p %{buildroot}%{_datadir}/inkscape/extensions
ln -s %{python3_sitelib}/%{srcname}/tikz_export.py \
  %{buildroot}%{_datadir}/inkscape/extensions/tikz_export.py
ln -s %{python3_sitelib}/%{srcname}/tikz_export_effect.inx \
  %{buildroot}%{_datadir}/inkscape/extensions/tikz_export_effect.inx
ln -s %{python3_sitelib}/%{srcname}/tikz_export_output.inx \
  %{buildroot}%{_datadir}/inkscape/extensions/tikz_export_output.inx

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%{_bindir}/svg2tikz
# Poetry does not mark license files
# https://github.com/python-poetry/poetry/issues/1350
#%license %{python3_sitelib}/svg2tikz-2.1.0.dist-info/LICENSE

%files -n inkscape-%{srcname}
%license LICENSE
# co-own directory with Inkscape
%dir %{_datadir}/inkscape/extensions
%{_datadir}/inkscape/extensions/tikz_export.py
%{_datadir}/inkscape/extensions/tikz_export_effect.inx
%{_datadir}/inkscape/extensions/tikz_export_output.inx


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 02 2024 Benson Muite <benson_muite@emailplus.org> - 3.2.0-2
- Update paths

* Tue Oct 01 2024 Benson Muite <benson_muite@emailplus.org> - 3.2.0-1
- Update to release 3.2.0

* Mon Sep 30 2024 Benson Muite <benson_muite@emailplus.org> - 2.1.0-7
- Fix broken symlinks

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.1.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 Lumír Balhar <lbalhar@redhat.com> - 2.1.0-2
- Remove version limit from lxml

* Thu Sep 07 2023 Benson Muite <benson_muite@emailplus.org> - 2.1.0-1
- Initial packaging
