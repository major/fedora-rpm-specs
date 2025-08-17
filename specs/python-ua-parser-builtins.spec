%global pkg_name ua-parser-builtins

Name:           python-%{pkg_name}
Version:        0.18.0.post1
Release:        4%{?dist}
Summary:        Precompiled rules for User Agent Parser

License:        Apache-2.0
URL:            https://github.com/ua-parser/uap-python
BuildArch:      noarch
# git clone --recursive https://github.com/ua-parser/uap-python.git ua_parser
# cd ua_parser/ua-parser-builtins
# cp ../LICENSE .
# python3 -m build --sdist
# cp dist/ua_parser_builtins-%%{version}.tar.gz ../../
# NOTE: Requested upstream to publish a sdist archive and add a LICENSE file:
# => https://github.com/ua-parser/uap-python/issues/262
Source0:        ua_parser_builtins-%{version}.tar.gz

BuildRequires:  python3-devel


%description
Precompiled rules for User Agent Parser.


%package -n python3-%{pkg_name}
Summary:        Precompiled rules for User Agent Parser


%description -n python3-%{pkg_name}
Precompiled rules for User Agent Parser.


%prep
%autosetup -p1 -n ua_parser_builtins-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ua_parser_builtins


%check
# %%pyproject_check_import cannot be run because of circular dependency on ua-parser


%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md


%changelog
* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.18.0.post1-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0.post1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 11 2025 Python Maint <python-maint@redhat.com> - 0.18.0.post1-2
- Rebuilt for Python 3.14

* Sun Mar 23 2025 Sandro Mani <manisandro@gmail.com> - 0.18.0.post1-1
- Initial package
