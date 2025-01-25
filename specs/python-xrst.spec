# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/


# Fedora Release starts with 1; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/
Name:           python-xrst
Version:        2025.0.2
Release:        3%{?dist}
Summary:        Extract Sphinx RST Files

License:        GPL-3.0-or-later
URL:            https://github.com/bradbell/xrst
Source:         %{url}/archive/%{version}/python-xrst-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a sphinx wrapper that extracts RST files from source code
and then runs sphinx to obtain html, tex, or pdf output files.
It includes automatic processing and commands that make sphinx easier to use.}

# First %%description command.
%description %_description

%package -n python3-xrst
Summary:        %{summary}

# Second %%description command.
# What is the difference between the two %%description commands ?
%description -n python3-xrst %_description

%prep
%autosetup -p1 -n xrst-%{version}
#
# Suppress spelling warnings during tox because this system
# may use a different dictionary than is used for xrst development.
cat << EOF > temp.sed
s|'sphinx_rtd_theme'|&, '--suppress_spell_warnings'|
EOF
sed -i pytest/test_rst.py -f temp.sed 
#
# Change toml -> tomli
# This patch will not be necessary when version >= 2026.0.0
cat << EOF > temp.sed
s|import toml\$|import tomli|
s|toml[.]loads[(]|tomli.loads(|
s|^( *)toml\$|\\1tomli|
s|'toml'|'tomli'|
EOF
#
for file in \
   bin/rst2man.py \
   pyproject.toml \
   tox.ini \
   xrst/auto_file.py \
   xrst/get_conf_dict.py \
   xrst/rename_group.py \
   xrst/replace_spell.py \
   xrst/run_xrst.py
do
   sed -r -i $file -f temp.sed
done
#
%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files xrst

# -----------------------------------------------------------------------------
# Do after installs above so don't get an rpmlint warning about using buildroot
#
# create %%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man1
#
# create build/rst/run_xrst.rst
%{python3} -m xrst \
   --rst_only --group_list default user --suppress_spell_warnings
#
# install %%{_mandir}/man1/xrst.1
%{python3} bin/rst2man.py \
   build/rst/run_xrst.rst %{buildroot}/%{_mandir}/man1/xrst.1
# -----------------------------------------------------------------------------

%check
%tox
#

%files -n python3-xrst -f %{pyproject_files}
%doc readme.md
%license gpl-3.0.txt

# xrst executable
%{_bindir}/xrst

# xrst.1 man page
%{_mandir}/man1/xrst.1*

%changelog
* Thu Jan 23 2025 Brad Bell <bradbell at seanet dot com> - 2025.0.2-3
- Change import toml -> import tomli; see
- https://fedoraproject.org/wiki/Changes/DeprecatePythonToml

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2025.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Brad Bell <bradbell at seanet dot com> - 2025.0.2-1
- New upstream source.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2024.0.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 06 2024 Brad Bell <bradbell at seanet dot com> - 2024.0.0-1
- New upstream source.
- pyspellchecker is now available as a fedora package.
- Remove some extra blank lines.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2023.1.22-2
- Rebuilt for Python 3.12

* Sun Jan 22 2023 Brad Bell <bradbell at seanet dot com> - 2023.1.22-1
- Update to new upstream source to help with building rpm for cppad-doc.
- Need to remove pyspellchecker from more places.

* Fri Jan 20 2023 Brad Bell <bradbell at seanet dot com> - 2023.1.9-1
- Fix spelling errror -> error
- Change python3 to %%{python} as 'Mandatory macors' in of python guidelines
- Include license file in files section
- Change bin/rst2man.py -> %%{python3} bin/rst2man.py
- rename this file from xrst.spec to python-xrst.spec
