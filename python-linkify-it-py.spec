# It is not currently possible to build the documentation, because Fedora
# lacks sphinx_book_theme.

Name:           python-linkify-it-py
Version:        2.0.2
Release:        1%{?dist}
Summary:        Link recognition library with full Unicode support

License:        MIT
URL:            https://github.com/tsutsu3/linkify-it-py
Source0:        %{url}/archive/v%{version}/linkify-it-py-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This is a Python port of linkify-it [1], a link recognition library with
FULL unicode support.  It is focused on high quality link pattern
detection in plain text.  See a JavaScript demo [2].

References:
[1] https://github.com/markdown-it/linkify-it
[2] https://markdown-it.github.io/linkify-it/}

%description %_description

%package     -n python3-linkify-it-py
Summary:        Link recognition library with full Unicode support

%description -n python3-linkify-it-py %_description

%prep
%autosetup -n linkify-it-py-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files linkify_it

%check
%pytest

%files -n python3-linkify-it-py -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
* Tue May  2 2023 Jerry James <loganjerry@gmail.com> - 2.0.2-1
- Version 2.0.2

* Mon May  1 2023 Jerry James <loganjerry@gmail.com> - 2.0.1-1
- Version 2.0.1

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 2.0.0-2
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Initial RPM
