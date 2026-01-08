Name:           R-R6
Version:        %R_rpm_version 2.6.1
Release:        %autorelease
Summary:        Classes with Reference Semantics

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
The R6 package allows the creation of classes with reference semantics,
similar to R's built-in reference classes. Compared to reference classes,
R6 classes are simpler and lighter-weight, and they are not built on S4
classes so they do not require the methods package. These classes allow
public and private members, and they support inheritance, even when the
classes are defined in different packages.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
