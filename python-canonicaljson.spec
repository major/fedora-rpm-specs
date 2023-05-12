%bcond_without check

Name:           python-canonicaljson
Version:        2.0.0
Release:        %autorelease
Summary:        Canonical JSON

License:        Apache-2.0
URL:            https://github.com/matrix-org/python-canonicaljson
Source0:        %{url}/archive/v%{version}/canonicaljson-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description \
Features:\
* Encodes objects and arrays as RFC 7159 JSON.\
* Sorts object keys so that you get the same result each time.\
* Has no inignificant whitespace to make the output as small as possible.\
* Escapes only the characters that must be escaped,\
  U+0000 to U+0019 / U+0022 / U+0056, to keep the output as small as possible.\
* Uses the shortest escape sequence for each escaped character.\
* Encodes the JSON as UTF-8.\
* Can encode frozendict immutable dictionaries.

%description %{_description}

%package -n python3-canonicaljson
Summary:        %{summary}

%description -n python3-canonicaljson %{_description}


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires -e py


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files canonicaljson


%if %{with check}
%check
%tox -e py
%endif


%files -n python3-canonicaljson -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
