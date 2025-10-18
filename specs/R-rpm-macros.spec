Name:           R-rpm-macros
Version:        1.2.1
Release:        %autorelease
Summary:        Macros to help produce R packages

License:        MIT
URL:            https://github.com/rpm-software-management/R-rpm-macros
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
Requires:       R-core
Requires:       rpm

%description
This package contains the R RPM macros, that most implementations should rely
on.

You should not need to install this package manually as the R-devel package
requires it. So install the R-devel package instead.


%prep
%autosetup -p1


%install
%make_install PREFIX=%{_prefix}


%files
%doc README.md
%license LICENSE
%{_rpmconfigdir}/fileattrs/R.attr
%{_rpmconfigdir}/R-deps.R


%changelog
%autochangelog
