%global srcname parse

Name:           python-%{srcname}
Version:        1.19.0
Release:        %autorelease
Summary:        Opposite of format()

License:        BSD
URL:            http://pypi.python.org/pypi/parse
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description \
Parse strings using a specification based on the Python format() syntax.\
\
"parse()" is the opposite of "format()"

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%python3 test_parse.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
