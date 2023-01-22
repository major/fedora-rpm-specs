# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/

Name:           python-xrst
Version:        2023.1.9
Release:        1%{?dist}
Summary:        Extract Sphinx RST Files

License:        GPL-3.0-or-later
URL:            https://github.com/bradbell/xrst
Source:         %{url}/archive/%{version}/xrst-%{version}.tar.gz

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

# -----------------------------------------------------------------------------
# tox.ini
# Using rmpbuild -ba SPECS/xrst.spec on 6.0.15-200.fc36.x86_64:
# .1 If we do not remove pyspellchecker from tox.ini we get error the message
#    python3dist(pyspellchecker) is needed by python-xrst ...
# 2. If we try dnf install 'python3dist(pyspellchecker)' we get the message
#    No match for argument: python3dist(pyspellchecker)
# 3. If we try pip install pyspellchecker we get the message
#    Requirement already satisfied: ...
sed -i tox.ini -e '/^ *pyspellchecker$/d'
# -----------------------------------------------------------------------------

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
%{python3} -m xrst --rst_only --group_list default user
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
* Fri Jan 20 2023 Brad Bell <bradbell at seanet dot com> - 2023.1.9-1
- Fix spelling errror -> error
- Change python3 to %%{python} as 'Mandatory macors' in of python guidelines
- Include license file in files section
- Change bin/rst2man.py -> %%{python3} bin/rst2man.py
- rename this file from xrst.spec to python-xrst.spec
