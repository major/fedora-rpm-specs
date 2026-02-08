Name:           python-chevron
Version:        0.14.0
Release:        %autorelease
Summary:        Mustache templating language renderer

License:        MIT
URL:            https://github.com/noahmorrison/chevron
Source:         %{pypi_source chevron}
Source1:        LICENSE

BuildSystem:    pyproject
BuildOption(install):  -L chevron

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
A python implementation of the mustache templating language.}

%description %_description

%package -n     python3-chevron
Summary:        %{summary}

%description -n python3-chevron %_description

%prep -a
cp %{SOURCE1} .

%install -a
sed -i '1s|#!/usr/bin/python|#!/usr/bin/python3|' %{buildroot}%{python3_sitelib}/chevron/main.py
chmod a+x %{buildroot}%{python3_sitelib}/chevron/main.py 

%check
%pyproject_check_import

%files -n python3-chevron -f %{pyproject_files}
%license LICENSE
%{_bindir}/chevron

%changelog
%autochangelog
