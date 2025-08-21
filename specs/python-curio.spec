# Upstream doesn't plan to make any more releases.  Unless they change their
# mind, we'll need to stick with git snapshots going forward.
# https://github.com/dabeaz/curio/commit/45ada857189de0e6b3b81f50e93496fc710889ca
%global commit      148454621f9bd8dd843f591e87715415431f6979
%global shortcommit %{sub %{commit} 1 7}

Name:           python-curio
Version:        1.6^1.%{shortcommit}
Release:        %autorelease
Summary:        Building blocks for performing concurrent I/O
License:        BSD-3-Clause
URL:            https://github.com/dabeaz/curio
Source:         %{url}/archive/%{commit}/curio-%{shortcommit}.tar.gz
BuildArch:      noarch

%global common_description %{expand:
Curio is a coroutine-based library for concurrent Python systems programming
using async/await. It provides standard programming abstractions such as tasks,
sockets, files, locks, and queues as well as some advanced features such as
support for structured concurrency. It works on Unix and Windows and has zero
dependencies. You will find it to be familiar, small, fast, and fun.}


%description %{common_description}


%package -n python3-curio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}


%description -n python3-curio %{common_description}


%prep
%autosetup -n curio-%{commit}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files curio


%check
# test_cpu is flaky
# https://github.com/dabeaz/curio/issues/368
%pytest --verbose -m 'not internet' -k 'not test_cpu'


%files -n python3-curio -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
