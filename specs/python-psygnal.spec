Name:           python-psygnal
Version:        0.15.1
Release:        %autorelease
Summary:        Fast python callback/event system modeled after Qt Signals

License:        BSD-3-Clause
URL:            https://github.com/pyapp-kit/psygnal
Source:         %{pypi_source psygnal}

BuildSystem:    pyproject
BuildOption(install): -l psygnal
BuildOption(generate_buildrequires): -g test-min,test

BuildArch:      noarch

%global _description %{expand:
Psygnal (pronounced "signal") is a pure python implementation of the observer
pattern, with the API of Qt-style Signals with (optional) signature and type
checking, and support for threading. It has no dependencies.}

%description %_description

%package -n     python3-psygnal
Summary:        %{summary}

%description -n python3-psygnal %_description

%prep -a
sed -i '/pyinstaller/d' pyproject.toml

%check
%pytest -rs

%files -n python3-psygnal -f %{pyproject_files}

%changelog
%autochangelog