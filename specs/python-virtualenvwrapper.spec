%global modname virtualenvwrapper
%global desc virtualenvwrapper is a set of extensions to Ian Bicking's \
`virtualenv <http://pypi.python.org/pypi/virtualenv>`_ tool.  The extensions \
include wrappers for creating and deleting virtual environments and otherwise \
managing your development workflow, making it easier to work on more than \
one project at a time without introducing conflicts in their dependencies.
%global sum Enhancements to virtualenv

Name:             python-%{modname}
Version:          6.1.1
Release:          %autorelease
Summary:          %{sum}

License:          MIT
URL:              https://github.com/python-%{modname}/%{modname}
Source:           %{pypi_source %{modname}}

BuildArch:        noarch

BuildRequires:      python3-devel

## Just for tests
# BuildRequires:      zsh

%description
%{desc}

%package -n python3-%{modname}
Summary:            %{sum}

Requires:           which

%description -n python3-%{modname}
%{desc}

%prep
%autosetup -p1 -n %{modname}-%{version}
rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{modname}

# Prepend a shebang to these so they are not stripped of executable bits
sed -i '1i #!/bin/sh' %{buildroot}/%{_bindir}/%{modname}.sh

%{__mkdir_p} %{buildroot}/%{_sysconfdir}/profile.d/
ln -s %{_bindir}/virtualenvwrapper_lazy.sh %{buildroot}/%{_sysconfdir}/profile.d/virtualenvwrapper.sh

ln -s %{_bindir}/virtualenvwrapper_lazy.sh %{buildroot}/%{_bindir}/virtualenvwrapper_lazy-3.sh
ln -s %{_bindir}/virtualenvwrapper.sh %{buildroot}/%{_bindir}/virtualenvwrapper-3.sh


%check
# The tests are shell based, hence not reliable in an rpmbuild environment
%pyproject_check_import

%files -n python3-%{modname} -f %{pyproject_files}
%doc PKG-INFO docs README.txt
%license LICENSE
%{_bindir}/virtualenvwrapper.sh
%{_bindir}/virtualenvwrapper_lazy.sh
%{_bindir}/virtualenvwrapper-3.sh
%{_bindir}/virtualenvwrapper_lazy-3.sh
%config(noreplace) %{_sysconfdir}/profile.d/virtualenvwrapper.sh

%changelog
%autochangelog
