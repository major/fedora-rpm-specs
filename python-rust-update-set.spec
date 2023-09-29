%global modname rust_update_set
%global srcname %{py_dist_name %modname}

Name:           python-%{srcname}
Version:        0.0.1
Release:        %autorelease
Summary:        A tool to help Fedora packagers update Rust packages

License:        MIT
URL:            https://pagure.io/fedora-rust/rust-update-set
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# proposed patch to port from removed rust2rpm APIs to cargo2rpm
# https://pagure.io/fedora-rust/rust-update-set/pull-request/11
# FIXME: likely an incomplete port, it just makes the tests pass
Patch:          %{url}/pull-request/11.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
rust-update-set is a Fedora packager tool which tries to automate some common tasks
like:

- recursively check out all packages that need to be updated or missing deps that need to be packaged
- preserve changes in old spec file when updating spec file using rust2rpm
- check update compatibility and create packages with suffix when a transitive closure is introduced
- automate parallel COPR builds of sets of packages in dependency order
- chain-build all packages in Koji with requested side tag
- merging and chain-building all packages across release branches
- create compat crate rust-{crate}{older} when updating some packages will break other packages.}

%description %_description


%package -n %{srcname}
Summary:        %{summary}
Requires:       copr-cli

%description -n %{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{modname}


%check
%pytest


%files -n %{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{srcname}


%changelog
%autochangelog
