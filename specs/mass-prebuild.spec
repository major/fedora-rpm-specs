Name:           mass-prebuild
Version:        1.8.0
Release:        %autorelease
Summary:        A set of tools to massively pre-build reverse dependencies for an RPM package

License:        GPL-2.0-or-later
URL:            https://gitlab.com/fedora/packager-tools/mass-prebuild
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

Patch:          0001-fix-Improve-package-committish-resolution-logic.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-dnf

BuildRequires:  rubygem(asciidoctor)
BuildRequires:  make
BuildRequires:  mock

Requires: copr-cli
Requires: (python3-libdnf or python3-libdnf5)
Requires: fedpkg
Requires: mock

Provides: mpb = %{version}-%{release}
Provides: mpb-whatrequires = %{version}-%{release}
Provides: mpb-failedconf = %{version}-%{release}
Provides: mpb-copr-edit = %{version}-%{release}
Provides: mpb-report = %{version}-%{release}


%description
The mass pre-builder tool is a set of helper tools that for the user to
build a package using COPR, calculate a list of reverse dependencies for this
package, build these reverse dependencies against the new version of the main
package and give a report on failures to be manually assessed.


%prep
%autosetup -p1 -n %{name}-v%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
mkdir -p bash_completion.d
echo "$(register-python-argcomplete mpb)" > bash_completion.d/mpb.bash
echo "$(register-python-argcomplete mpb-copr-edit)" > bash_completion.d/mpb-copr-edit.bash
echo "$(register-python-argcomplete mpb-failedconf)" > bash_completion.d/mpb-failedconf.bash
echo "$(register-python-argcomplete mpb-report)" > bash_completion.d/mpb-report.bash
echo "$(register-python-argcomplete mpb-whatrequires)" > bash_completion.d/mpb-whatrequires.bash
pushd man
%make_build
popd


%install
%pyproject_install
install -d %{buildroot}%{bash_completions_dir}
install -pm0644 bash_completion.d/* %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{_sysconfdir}/mpb
cp -r examples/*.conf.d %{buildroot}%{_sysconfdir}/mpb
mkdir -p %{buildroot}%{_mandir}/man1
cp -r man/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
cp -r man/*.5 %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man7
cp -r man/*.7 %{buildroot}%{_mandir}/man7

%pyproject_save_files -l mass_prebuild


%check
# MPB is a tool using DNF/Koji/Copr-cli:
# There is no meaningful test that could be executed without internet access.
%{py3_test_envvars} mpb --version
%{py3_test_envvars} mpb-whatrequires --version
%{py3_test_envvars} mpb-failedconf --version
%{py3_test_envvars} mpb-copr-edit --version
%{py3_test_envvars} mpb-report --version


%files -f %{pyproject_files}
%dir %{_sysconfdir}/mpb
%dir %{_sysconfdir}/mpb/*.conf.d
%config(noreplace) %{_sysconfdir}/mpb/*.conf.d/*
%{bash_completions_dir}/mpb*
%doc README.md examples
%{_mandir}/man1/mpb*.1*
%{_mandir}/man5/mpb*.5*
%{_mandir}/man7/mass-prebuild.7*
%{_bindir}/mpb
%{_bindir}/mpb-whatrequires
%{_bindir}/mpb-failedconf
%{_bindir}/mpb-copr-edit
%{_bindir}/mpb-report


%changelog
%autochangelog
