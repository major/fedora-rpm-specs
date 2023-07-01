# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/

Name:           python-xrst
Version:        2023.1.22
Release:        2%{?dist}
Summary:        Extract Sphinx RST Files

License:        GPL-3.0-or-later
URL:            https://github.com/bradbell/xrst
Source:         %{url}/archive/%{version}/python-xrst-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-enchant
BuildRequires:  python3-docutils

%global _description %{expand:
This is a sphinx wrapper that extracts RST file from source code
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
# not yet available on fedora
sed -i tox.ini        -e '/^ *pyspellchecker$/d'
sed -i pyproject.toml -e "s|'pyspellchecker',||" -e "s|'sphinx-book-theme',||"
sed -i setup.py       -e "s|'pyspellchecker',||" -e "s|'sphinx-book-theme',||"
#
# Suppress spelling warnings during pytest because this system
# uses a different dictionary.
sed -i pytest/test_rst.py \
   -e "s|'sphinx_rtd_theme',|&\n      '--suppress_spell_warnings',|"
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
