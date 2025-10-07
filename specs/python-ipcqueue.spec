Name:           python-ipcqueue
Version:        0.9.7
Release:        %autorelease
Summary:        POSIX and SYS V message queues to exchange data among processes
License:        BSD-3-Clause
URL:            https://pypi.org/project/ipcqueue/
Source0:        %{pypi_source ipcqueue}
Patch:          https://github.com/seifert/ipcqueue/pull/10.patch

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides SYS V and POSIX message queues to exchange data among
processes. Both queues have similar functionality with some differences. Queues
are persistent in the kernel unless either queue is closed/unlinked or system
is shut down. Unlike multiprocessing.Queue, the same queue can be joined by
different processes according to its unique name/key, it’s not necessary to
fork main process.}

%description %_description

%package -n python3-ipcqueue
Summary:        %{summary}

%description -n python3-ipcqueue %_description

%package doc
Summary:       HTML documention for python3-ipcqueue
BuildArch:     noarch

%description doc
%{summary}.

%prep
%autosetup -p1 -n ipcqueue-%{version}

%generate_buildrequires
%pyproject_buildrequires

# for the docs
echo "python3dist(sphinx-rtd-theme)"
echo "python-sphinx"
echo "make"

%build
%pyproject_wheel

make -C doc html man
rm doc/_build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files -l ipcqueue
install -D -m 0644 doc/_build/man/ipcqueue.1 %{buildroot}%{_mandir}/man3/ipcqueue.3

%check
%pytest

%files -n  python3-ipcqueue -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%{_mandir}/man3/ipcqueue.3*

%files doc
%doc doc/_build/html

%changelog
%autochangelog
