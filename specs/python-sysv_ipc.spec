%global srcname sysv_ipc
%global sum System V IPC for Python - Semaphores, Shared Memory and Message Queues
%global desc The sysv_ipc module which gives Python access to System V inter-process\
semaphores, shared memory and message queues on systems that support them.

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        %{sum}
License:        GPL-3.0-or-later
URL:            http://semanchuk.com/philip/%{srcname}/
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel


%description
%{desc}


%package examples
Summary:    Examples for Python sysv_ipc module


%description examples
This module comes with four demonstration apps. 


%package -n python3-%{srcname}
Summary:        %{sum}


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n sysv_ipc-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files sysv_ipc

chmod -x demos/*/*.{py,sh}


%check
%pyproject_check_import sysv_ipc


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE 
%doc README.md USAGE.md


%files examples
%doc demos


%changelog
%autochangelog
