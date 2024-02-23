Name:           python-opentelemetry-propagator-aws-xray
Version:        1.0.1
Release:        %autorelease -b 52
Summary:        AWS X-Ray Propagator for OpenTelemetry

# PyPI source distributions lacks tests; use the GitHub archive even though it
# includes many other packages maintained in the same repository
%global forgeurl https://github.com/open-telemetry/opentelemetry-python-contrib
# Having the equals character appear in the source filename breaks everything,
# and the build breaks because a source named %%{version}.tar.gz is not
# present. Using the url-escaped version of the tag is a workaround.
%global tag opentelemetry-propagator-aws-xray%%3D%%3D%{version}
# As a peculiarity of GitHub when the tag contains the equals character, the
# archive name (and the name of the directory containing the extracted sources)
# does not exactly match the tag.
%global extractdir opentelemetry-python-contrib-%(echo '%{tag}' | sed -r 's/(%%3D)+/-/')

License:        Apache-2.0
URL:            https://pypi.org/project/opentelemetry-propagator-aws-xray
Source:         %{forgeurl}/archive/%{tag}/%{extractdir}.tar.gz

# Add missing test dep. on requests for xray propagator
# https://github.com/open-telemetry/opentelemetry-python-contrib/pull/2167
# Cherry-picked to tag opentelemetry-propagator-aws-xray==1.0.1 (before
# conversion to pyproject.toml).
Patch:          0001-Add-missing-test-dep.-on-requests-for-xray-propagato.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# Maintaining manual test dependencies is easier than trying to generate them
# from the top-level tox.ini.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-benchmark}

%global common_description %{expand:
This library provides the propagator necessary to inject or extract a tracing
context across AWS services.}

%description %{common_description}


%package -n python3-opentelemetry-propagator-aws-xray
Summary:        %{summary}

%description -n python3-opentelemetry-propagator-aws-xray %{common_description}


%prep
%autosetup -p1 -n %{extractdir}


%generate_buildrequires
cd propagator/opentelemetry-propagator-aws-xray
%pyproject_buildrequires -x test


%build
cd propagator/opentelemetry-propagator-aws-xray
%pyproject_wheel


%install
cd propagator/opentelemetry-propagator-aws-xray
%pyproject_install
# The opentelemetry and opentelemetry/propagators directies are shared
# namespace package directories; they are co-owned with other opentelemetry
# packages, including subpackages of python-opentelemetry and/or
# python-opentelemetry-contrib. See RHBZ#1935266.
%pyproject_save_files -l opentelemetry


%check
cd propagator/opentelemetry-propagator-aws-xray
%pytest -v


%files -n python3-opentelemetry-propagator-aws-xray -f %{pyproject_files}
#license propagator/opentelemetry-propagator-aws-xray/LICENSE
%doc propagator/opentelemetry-propagator-aws-xray/README.rst

# Shared namespace directories; these are co-owned with other opentelemetry
# packages, including subpackages of python-opentelemetry and/or
# python-opentelemetry-contrib.
#dir #{python3_sitelib}/opentelemetry/{,propagators/}

#{python3_sitelib}/opentelemetry/propagators/aws/
#global aws_propagator_distinfo #(echo '#{aws_propagator_version}' | tr -d '~^').dist-info
#{python3_sitelib}/opentelemetry_propagator_aws_xray-#{aws_propagator_distinfo}/


%changelog
%autochangelog
