%global modname evalidate

Name:           python-%{modname}
Version:        2.0.5
Release:        %autorelease
Summary:        Safe and very fast eval()'uating user-supplied python expressions

License:        MIT
URL:            https://github.com/yaroslaff/evalidate
Source:         %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Evalidate is simple python module for safe and very fast eval()'uating user-
supplied (possible malicious) python expressions.}

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %_description


%prep
%autosetup -p1 -n %{modname}-%{version}
# Remove unneded shebang
sed -i -e '/^#!/,1d' evalidate/__init__.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{modname}


%check
%pytest -v


%files -n python3-%{modname} -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
