%global srcname drf-yasg

Name:           python-%{srcname}
Version:        1.20.0
%global pyversion %(v=%{version}; echo ${v%%.0*})
Release:        7%{?dist}
Summary:        Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest

# Not all license texts are included: https://github.com/axnsan12/drf-yasg/issues/536
License:        BSD and MIT and ASL 2.0
URL:            https://github.com/axnsan12/drf-yasg
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Automated generation of real Swagger/OpenAPI 2.0 schemas
from Django Rest Framework code.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
# src/drf_yasg/static/immutable.min.js
# License(s): MIT
Provides:       bundled(js-immutable)
# src/drf_yasg/static/insQ.min.js
# License(s): MIT
Provides:       bundled(js-insertion-query) = 1.0.3
# src/drf_yasg/static/redoc/
# License(s): MIT
Provides:       bundled(js-redoc) = 2.0.0~rc.40
# src/drf_yasg/static/redoc-old/
# License(s): MIT
Provides:       bundled(js-redoc) = 1.22.3
# src/drf_yasg/static/swagger-ui-dist/
# License(s): ASL 2.0
Provides:       bundled(js-swagger-ui-dist) = 3.36.0

%description -n python3-%{srcname} %{_description}

Python 3 version.

%package     -n python3-%{srcname}+validation
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+validation}
Provides:       python3dist(%{srcname}/validation) = %{pyversion}
Provides:       python%{python3_version}dist(%{srcname}/validation) = %{pyversion}
Requires:       python%{python3_version}dist(%{srcname}) = %{pyversion}
Requires:       python%{python3_version}dist(swagger-spec-validator) >= 2.1.0

%description -n python3-%{srcname}+validation %{_description}

"validation" extras. Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr src/*.egg-info

%build
%py3_build

%install
%py3_install

# Tests require too many dependencies
#%%check
#%%python3 -m pytest -v

%files -n python3-%{srcname}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/drf_yasg/
%{python3_sitelib}/drf_yasg-*.egg-info/

%files -n python3-%{srcname}+validation
%{?python_extras_subpkg:%ghost %{python3_sitelib}/drf_yasg-*.egg-info/}

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.20.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.20.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-3
- Add metadata for Python extras subpackages

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.17.0-1
- Initial package
