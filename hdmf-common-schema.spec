# This package should be updated together with python-hdmf to ensure
# compatibility. Note that it currently depends on an exact version of this
# package.

Name:           hdmf-common-schema
Version:        1.8.0
Epoch:          1
Release:        %autorelease
Summary:        Specifications for pre-defined data structures provided by HDMF

License:        BSD-3-Clause-LBNL
URL:            https://github.com/hdmf-dev/hdmf-common-schema
Source:         %{url}/archive/%{version}/hdmf-common-schema-%{version}.tar.gz

BuildArch:      noarch

%description
The HDMF Common specification defines a collection of common, reusable data
structures that build the foundation for the modeling of advanced data formats,
e.g., the Neurodata Without Borders (NWB) (https://www.nwb.org/)
neurophysiology data standard. The HDMF Common schema is integrated with HDMF
(https://github.com/hdmf-dev/hdmf), which provides advanced APIs for reading,
writing, and using HDMF-common data types.


%prep
%autosetup


# We could build and install the associated documentation, but we would have to
# package python-hdmf-docutils to do so.
#
# Note that we would need to build PDF documentation, as Sphinx-generated HTML
# documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555, the linked devel mailing
# list thread, and https://pagure.io/packaging-committee/pull-request/1244, for
# discussion.
#
# Overall, it doesn’t seem worthwhile.
#
# If we are not building documentation, then there is nothing to build.


%install
# There is no build-system script or standard install location for the schemas.
install -d '%{buildroot}%{_datadir}/hdmf-common-schema'
cp -rp 'common/' '%{buildroot}%{_datadir}/hdmf-common-schema/'


%files
%license license.txt Legal.txt
%doc README.md

%dir %{_datadir}/hdmf-common-schema/
%dir %{_datadir}/hdmf-common-schema/common/
%{_datadir}/hdmf-common-schema/common/*.yaml


%changelog
%autochangelog
