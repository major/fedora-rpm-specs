Name:           python-quart
Version:        0.20.0
Release:        %autorelease
Summary:        A Python ASGI web microframework with the same API as Flask

# SPDX
License:        MIT
URL:            https://github.com/pallets/quart
# PyPI source distributions lack tests, changelog, etc.; use the GitHub archive
Source:         %{url}/archive/%{version}/quart-%{version}.tar.gz
# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source10:       quart.1
Source11:       quart-routes.1
Source12:       quart-run.1
Source13:       quart-shell.1

# Downstream-only: patch out coverage analysis
# 
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# (This also patches out pytest-sugar because it’s unnecessary.)
Patch:          0001-Downstream-only-patch-out-coverage-analysis.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
Quart is an async Python web microframework. Using Quart you can,

  * render and serve HTML templates,
  * write (RESTful) JSON APIs,
  * serve WebSockets,
  * stream request and response data,
  * do pretty much anything over the HTTP or WebSocket protocols.}

%description %{common_description}


%package -n python3-quart
Summary:        %{summary}

%description -n python3-quart %{common_description}


%pyproject_extras_subpkg -n python3-quart dotenv


%prep
%autosetup -n quart-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -x dotenv requirements/tests.in


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l quart

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'


%check
%pytest -v


%files -n python3-quart -f %{pyproject_files}
%doc CHANGES.md
%doc README.md

%{_bindir}/quart
%{_mandir}/man1/quart{,-*}.1*


%changelog
%autochangelog
