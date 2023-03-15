%global pymodule_name openscap_report

Name:           openscap-report
Version:        0.2.1
Release:        1%{?dist}
Summary:        A tool for generating human-readable reports from (SCAP) XCCDF and ARF results

# The entire source code is LGPL-2.1+ and GPL-2.0+ and MIT except schemas/ and assets/, which are Public Domain
License:        LGPLv2+ and GPLv2+ and MIT and Public Domain
URL:            https://github.com/OpenSCAP/%{name}
Source0:        https://github.com/OpenSCAP/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

Provides:       bundled(patternfly) = 4

Requires:       python3-lxml
Requires:       redhat-display-fonts
Requires:       redhat-text-fonts

%global _description %{expand:
This package provides a command-line tool for generating
human-readable reports from SCAP XCCDF and ARF results.}

%description %_description


%prep
%autosetup -p1 -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
sphinx-build -b man docs _build_docs



%install
%pyproject_install
%pyproject_save_files %{pymodule_name}
install -m 0644 -Dt %{buildroot}%{_mandir}/man1 _build_docs/oscap-report.1


%check
%tox

%files -f %{pyproject_files}
%{_mandir}/man1/oscap-report.*
%{_bindir}/oscap-report
%exclude %{python3_sitelib}/tests/
%license LICENSE


%changelog
* Mon Mar 13 2023 Packit <hello@packit.dev> - 0.2.1-1
- 0.2.1 (Jan Rodak)
- Add rule weight attribute to report (Jan Rodak)
- Parse rule weight attribute (Jan Rodak)
- Add weight attribute to rule datastructure (Jan Rodak)

* Wed Mar 08 2023 Packit <hello@packit.dev> - 0.2.0-0
- 0.2.0 (Jan Rodak)
- Add JSON validator tool (Jan Rodak)
- Create tests (Jan Rodak)
- Update issue templates (Jan Rodák)
- Impruve run time of unit tests (Jan Rodak)
- Add funtion for filtering JSON (Jan Rodak)
- Filter JSON keys (Jan Rodak)
- Adapt the tests and create a new test that tests the validation (Jan Rodak)
- Add an unsupported XML format to the result (Jan Rodak)
- Create validation of XCCDF files (Jan Rodak)
- Add XCCDF schemas (Jan Rodak)
- Fix typo in variable name (Jan Rodak)
- Fix problem that was spotted with new test and create test case (Jan Rodak)
- Add testcase of the crash when is used XCCDF result (Jan Rodak)
- Impruve raised expection info (Jan Rodak)
- Hide empty info about profile when isnt anvalible (Jan Rodak)
- Add missing else branch for if condition if is cpe_platform not defined in jinja (Jan Rodak)
- Add unit tests for SharedStaticMethodsOfParser (Jan Rodak)
- Add check and check_existence atributes to report (Jan Rodak)
- Add information about OVAL state to report (Jan Rodak)
- Decompose OVALTestInfoParser class (Jan Rodak)
- Parse OVAL state (Jan Rodak)
- Add OVAL state class (Jan Rodak)
- Add info about comparison of endpoint values in OVAL test (Jan Rodak)
- Ignore deprecated settings of pylint (Jan Rodak)
- Update tests (Jan Rodak)
- Add category to report (Jan Rodak)
- Parse category of warning (Jan Rodak)
- Add Warning dataclass (Jan Rodak)
- Update pylint config (Jan Rodak)
- Reduce external dependencies of test suite (Jan Rodak)
- Fix data type (Jan Rodak)
- Change label of OVAL definition for CPE (Jan Rodak)
- Add HTML generation of CPE AL trees (Jan Rodak)
- Add css for CPE AL (Jan Rodak)
- Create place for graph with CPE AL (Jan Rodak)
- Integrate CPE AL parser (Jan Rodak)
- Create CPE AL parser (Jan Rodak)
- Add expection (Jan Rodak)
- Add imports to __init__ (Jan Rodak)
- Create cpe platform (Jan Rodak)
- Add cpe logical test (Jan Rodak)
- Create evaluation of CPE logical test (Jan Rodak)
- Use a more elegant way to copy dictionary (Jan Rodak)
- Disable automatic character escaping in jinja (Jan Rodak)
- Remove duplicite CPE trees for fedora platforms (Jan Rodak)
- Fix the classification of tests (Jan Rodak)
- Present new infromation in HTML report (Jan Rodak)
- Update test suite (Jan Rodak)
- Update jinja macros for new dataclasses (Jan Rodak)
- Replace jinja filter with methode call that use diffrent informations (Jan Rodak)
- Implement usage of TestResultOfScan and ProfileInfo dataclasses (Jan Rodak)
- Add parser of performed scan information (Jan Rodak)
- Create parser of profile information (Jan Rodak)
- Use new dataclasses in Report (Jan Rodak)
- Create ProfileInfo and TestResultOfScan dataclasses (Jan Rodak)
- Regenerate docs modules (Jan Rodak)
- Ignore old xslt codes for generating old style report for backwards compatibility (Jan Rodak)
- Fix CWE-79 (Jan Rodak)
- Fix overwrite attribute get_report_dict, which was previously defined in superclass (Jan Rodak)
- Explicitly import stdout, stdin with prefix sys (Jan Rodak)
- Close file after usage (Jan Rodak)
- Fix empty expections (Jan Rodak)
- Fix missing OVAL definitions in reports when is not present OVAL CPE checks (Jan Rodak)
- Fix key error platfrom without OVAL definition (Jan Rodak)
- Fix missing CPE checks (Jan Rodak)
- Update README.md (Evgeny Kolesnikov)
- Update README.md (Evgeny Kolesnikov)
- Fix parsing of checking engine result (Jan Rodak)
- Rename master branch to main in github action configs TODO : LINKS IN README etc. (Jan Rodak)
- Rename master branch to main in realase script (Jan Rodak)
- Move comment of OVAL nodes behind result label (Jan Rodak)
- Display OVAL definitions details in the HTML report (Jan Rodak)
- Display comments in OVAL graphs (Jan Rodak)
- Replace the empty rule title with the rule id (Jan Rodak)
- Add srpm_build_deps (Jan Rodak)
- Update nodejs actions (Jan Rodak)
- Add CodeQL workflow for GitHub code scanning (LGTM Migrator)
- Add tests for oval definition (Jan Rodak)
- Reduce run time of test suite (Jan Rodak)
- Switch using oval_tree to oval_definition (Jan Rodak)
- Implement usage of OVAL definition parser (Jan Rodak)
- Create OVAL definition parser (Jan Rodak)
- Create OVAL reference (Jan Rodak)
- Create OVAL definition (Jan Rodak)
- Rename clases TestInfoParser to OVALTestInfoParser and OVALDefinitionParser to OVALResultParser (Jan Rodak)
- Add Read the Docs configuration file (Jan Rodak)
- Improve readme (Jan Rodak)
- Update chapter layout (Jan Rodak)
- Add usage chapter to documentation (Jan Rodak)
- Add installation chapter to documentation (Jan Rodak)
- Regenerate modules (Jan Rodak)
- Add link to readthedocs (Jan Rodak)
- Fix typo (Jan Rodak)
- Add instalation and basic usage to readme (Jan Rodak)
- Fix mixing of Rule class and rule XML element (Jan Rodak)
- Rename groupe_parser to group_parser and info_of_test_parser to test_info_parser (Jan Rodak)
- Create output format JSON-EVERYTHING (Jan Rodak)
- Use filter for generation JSON (Jan Rodak)
- Rename directory (Jan Rodak)
- Break methodes to smaller methods (Jan Rodak)
- Fix tests according to change of structure of SCAPResultsParser class (Jan Rodak)
- Rework structure SCAPResultsParser class (Jan Rodak)
- Rework assembly of OVAL and CPE trees (Jan Rodak)
- Remove None comment (Jan Rodak)
- Remove None value from definition ID (Jan Rodak)
- Fix test of remediation (Jan Rodak)
- Specify data types of Rule (Jan Rodak)
- Specify data types of Report (Jan Rodak)
- Remove default id of Remediation (Jan Rodak)
- Specify data types of OvalTest (Jan Rodak)
- Specify data types of OvalObject (Jan Rodak)
- Specify data types of OvalNode (Jan Rodak)
- Specify data types of Group (Jan Rodak)
- Create objects Identifier and Reference (Jan Rodak)
- Use buildin function asdict (Jan Rodak)
- Generate json output from report structure (Jan Rodak)
- Ignore generated JSON reports (Jan Rodak)
- Create tests (Jan Rodak)
- Use report_generators sub package (Jan Rodak)
- Create a JSON generator shell (Jan Rodak)
- Create report_generators sub package (Jan Rodak)
- Add format JSON to cli (Jan Rodak)
- Fix W1514 (Jan Rodak)
- Update pylint config (Jan Rodak)
- Add a copy to the clipboard for the rule ID field (Jan Rodak)
- Fix problem with the formatting of command line options (Jan Rodak)
- Replace default value TextIOWrapper with name of file in man page (Jan Rodak)
- Remove enumerte of choices for alternative options (Jan Rodak)
- Format lists of descriptions of choices (Jan Rodak)
- Fix FIRST_HIDDEN_ELEMENT is null (Jan Rodak)
- Remove unused template file (Jan Rodak)
- Move CSS style to separate file (Jan Rodak)
- Minimalize the usage of inline styles (Jan Rodak)
- Add footer to report (Jan Rodak)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Packit <hello@packit.dev> - 0.1.3-0
- 0.1.3 (Jan Rodak)
- Change license tag (Jan Rodak)
- Enable propose downstream (Jan Rodak)
- Add test for Full text parser (Jan Rodak)
- Add reproducer file for testing (Jan Rodak)
- Fix sub-element references that do not exist (Jan Rodak)

* Tue Aug 02 2022 Jan Rodak <jrodak@redhat.com> - 0.1.2-1
- Fix problems found by package review.

* Mon Jun 06 2022 Jan Rodak <jrodak@redhat.com> - 0.1.1-0
- Initial version of the package.
