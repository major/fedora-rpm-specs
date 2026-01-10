Name:           R-gmailr
Version:        %R_rpm_version 2.0.0
Release:        %autorelease
Summary:        Access the Gmail RESTful API

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
An interface to the Gmail RESTful API.  Allows access to your Gmail
messages, threads, drafts and labels.

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
