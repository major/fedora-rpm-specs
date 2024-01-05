%global srcname fedora-sig-onboard

Name:           python-%{srcname}
Version:        0.1.1
Release:        %autorelease
Summary:        Onboard a package onto the appropriate Fedora SIG

License:        MIT
URL:            https://pagure.io/fedora-sig-onboard
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
fedora-sig-onboard is a simple tool to onboard a Fedora package onto the
relevant SIG. It will attempt to add the SIG to the package ACL, update the
Bugzilla assignee and add the package to Anitya. Rust and Golang packages are
currently supported, and will be respectively onboarded onto the Rust SIG and
the Go SIG.}

%description %_description

%package -n     %{srcname}
Summary:        %{summary}

%description -n %{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fedora_sig_onboard

%check
%pyproject_check_import

%files -n %{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{srcname}

%changelog
%autochangelog
