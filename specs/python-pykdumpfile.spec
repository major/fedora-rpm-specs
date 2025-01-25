Name:           python-pykdumpfile
Version:        0.5.5.1
Release:        %autorelease
Summary:        Python bindings to libkdumpfile

License:        GPL-2.0-or-later
URL:            https://github.com/ptesarik/pykdumpfile
Source:         %{pypi_source pykdumpfile}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  gcc
BuildRequires:  libkdumpfile-devel


%global _description %{expand:
Bindings to the libkdumpfile shared library.}

%description %_description

%package -n     python3-pykdumpfile
Summary:        %{summary}
# provide an upgrade path until Fedora 41 is EOL
# we don't need to handle EL since python3-libkdumpfile is not published
%if 0%{?fedora} && 0%{?fedora} <= 43
Obsoletes:      python3-libkdumpfile < 0.5.5-1
%endif

%description -n python3-pykdumpfile %_description


%prep
%autosetup -p1 -n pykdumpfile-%{version}
# These are meant for Python 2 and wont' byte-compile
rm {addrxlat,kdumpfile}/defs_py2.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l addrxlat kdumpfile


%check
%pyproject_check_import
%pytest -v


%files -n python3-pykdumpfile -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_addrxlat%{python3_ext_suffix}
%{python3_sitearch}/_kdumpfile%{python3_ext_suffix}


%changelog
%autochangelog
