Name:           python-blurb
Version:        2.0.0
Release:        %autorelease
Summary:        Command-line tool to manage CPython Misc/NEWS.d entries

License:        BSD-3-Clause
URL:            https://github.com/python/blurb
Source:         %{pypi_source blurb %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
Blurb is a tool designed to rid CPython core development of the scourge of
Misc/NEWS conflicts.


%package -n     blurb
Summary:        %{summary}
%py_provides    python3-blurb
# This package was renamed from python3-blurb when it was updated to version 2
# The Obsoletes can be removed when Fedora 43 goes EOL
Obsoletes:      python3-blurb < 2~~

# Calls git in subprocess
Requires:       /usr/bin/git

%description -n blurb
Blurb is a tool designed to rid CPython core development of the scourge of
Misc/NEWS conflicts.


%prep
%autosetup -p1 -n blurb-%{version}
# avoid code coverage dependencies
sed -i '/"pytest-cov"/d' pyproject.toml

# script in site-packages
sed -i '1d' src/blurb/blurb.py
chmod -x src/blurb/blurb.py


%generate_buildrequires
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l blurb


%check
%pytest -v

%{py3_test_envvars} blurb --help
%{py3_test_envvars} %{python3} -m blurb --help


%files -n blurb -f %{pyproject_files}
%doc README.md
%{_bindir}/blurb


%changelog
%autochangelog
