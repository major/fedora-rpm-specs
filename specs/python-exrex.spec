Name:           python-exrex
Version:        0.12.0
Release:        %autorelease
Summary:        Irregular methods for regular expressions

License:        AGPL-3.0-or-later
URL:            https://github.com/asciimoo/exrex
Source:         %{url}/archive/v%{version}/exrex-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  help2man

%global _description %{expand:
Exrex is a command line tool and python module that generates all - or random -
matching strings to a given regular expression and more.}

%description %{_description}

%package -n     python3-exrex
Summary:        %{summary}

%description -n python3-exrex %{_description}

%prep
%autosetup -n exrex-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l exrex

# Rely on the generated entry point %%{_bindir}/exrex; do not package
# %%{_bindir}/exrex.py, which is a copy of the entire library. If something
# needs to execute exrex.py, we can add a symbolic or hard link with than name
# for compatibility.
rm '%{buildroot}%{_bindir}/exrex.py'

# The site-packages module does not have executable permissions, so it should
# not have a shebang line.
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/exrex.py'

# We need to do this in %%install rather than in %%build so we can use the
# %%{_bindir}/exrex entry point.
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
    --no-info \
    --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/exrex.1' \
    '%{buildroot}%{_bindir}/exrex'


%check
%tox

%files -n python3-exrex -f %{pyproject_files}
%doc README.md
%{_bindir}/exrex
%{_mandir}/man1/exrex.1*


%changelog
%autochangelog
