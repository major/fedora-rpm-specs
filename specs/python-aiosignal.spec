Name:           python-aiosignal
Version:        1.3.2
Release:        %autorelease
Summary:        List of registered asynchronous callbacks

License:        Apache-2.0
URL:            https://github.com/aio-libs/aiosignal
Source:         %{pypi_source aiosignal}

BuildSystem:            pyproject
BuildOption(install):   -l aiosignal

BuildArch:      noarch

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

%global common_description %{expand:
A project to manage callbacks in asyncio projects.}

%description %{common_description}


%package -n python3-aiosignal
Summary:        %{summary}

Obsoletes:      python-aiosignal-doc < 1.3.1-15

%description -n python3-aiosignal %{common_description}


%prep -a
# Patch out coverage options
sed -r -i 's/--cov[^[:blank:]]*//g' setup.cfg

# Do not fail on warnings
sed -zi 's/filterwarnings = error/filterwarnings = default/' setup.cfg


%check -a
%pytest


%files -n python3-aiosignal -f %{pyproject_files}
%doc CHANGES.rst
%doc CONTRIBUTORS.txt
%doc README.rst


%changelog
%autochangelog
