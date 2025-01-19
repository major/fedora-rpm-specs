%global pymodule_name openscap_report

Name:           openscap-report
Version:        1.0.0
Release:        2%{?dist}
Summary:        A tool for generating human-readable reports from (SCAP) XCCDF and ARF results

# The entire source code is LGPL-2.1+ and GPL-2.0+ and MIT except schemas/ and assets/, which are Public Domain
License:        LGPLv2+ and GPLv2+ and MIT and Public Domain
URL:            https://github.com/OpenSCAP/%{name}
Source0:        https://github.com/OpenSCAP/%{name}/releases/download/v%{version}/%{pymodule_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

Provides:       bundled(patternfly) = 4

Requires:       python3-lxml
Recommends:     redhat-display-fonts
Recommends:     redhat-text-fonts

Obsoletes:      oval-graph

%global _description %{expand:
This package provides a command-line tool for generating
human-readable reports from SCAP XCCDF and ARF results.}

%description %_description


%prep
%autosetup -p1 -n %{pymodule_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires
# test requirement listed only in tox.ini
echo "%{py3_dist jsonschema}"


%build
%pyproject_wheel
sphinx-build -b man docs _build_docs



%install
%pyproject_install
%pyproject_save_files %{pymodule_name}
install -m 0644 -Dt %{buildroot}%{_mandir}/man1 _build_docs/oscap-report.1


%check
# test_store_file fails with FileNotFoundError: [Errno 2] No such file or directory: '/tmp/oscap-report-tests_result.html'
%pytest -k "not test_store_file"

%files -f %{pyproject_files}
%{_mandir}/man1/oscap-report.*
%{_bindir}/oscap-report
%exclude %{python3_sitelib}/tests/
%license LICENSE


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 04 2024 Packit <hello@packit.dev> - 1.0.0-1
- Update to version 1.0.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.2.9-2
- Rebuilt for Python 3.13

* Tue Apr 23 2024 Packit <hello@packit.dev> - 0.2.9-1
- Update to version 0.2.9

* Mon Jan 29 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 0.2.7-2
- Avoid tox dependency

* Fri Jan 26 2024 Packit <hello@packit.dev> - 0.2.7-1
- 0.2.7 (Jan Rodak)
- Add tool tip to search bar (Jan Rodak)
- Enable search by reference (Jan Rodak)
- Add generation search infromation (Jan Rodak)
- Use macro for generation of list items (Jan Rodak)
- Create two-tier display of Evaluation Characteristics (Jan Rodak)
- Add title (Jan Rodak)
- Reduce complexity of function generate_referenced_endpoints (Jan Rodak)
- Use default dict (Jan Rodak)
- Fix JSON schema (Jan Rodak)
- Use correct orthography of addresses types acronyms (Jan Rodak)
- Add function to update known references (Jan Rodak)
- Change the presentation of referenced endpoints (Jan Rodak)
- Add new elements (Jan Rodak)
- Add onclick function (Jan Rodak)
- Add map of OVAL endpoints (Jan Rodak)
- Add target addresses to report (Jan Rodak)
- Add target addresses to model (Jan Rodak)
- Fix width of pre element (Jan Rodak)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Packit <hello@packit.dev> - 0.2.6-1
- 0.2.6 (Jan Rodak)
- Extend the condition to account empty strings in href (Jan Černý)
- Add comments for the pylint tool (Jan Černý)
- Add special classes to table element (Jan Černý)
- Account for missing reference href attribute (Jan Černý)
- Add pragmas to avoid PEP8 warnings (Jan Černý)
- Present references in a table (Jan Černý)
- Collapse CPE tree when is true (Jan Rodak)
- Fix typo (Jan Rodak)
- Add titles (Jan Rodak)
- Fix performace of generation of graphs (Jan Rodak)
- Rearrange fields of rule detail and OVAL definition detail (Jan Rodak)
- Fix bugs in html (Jan Rodak)

* Mon Sep 11 2023 Packit <hello@packit.dev> - 0.2.5-1
- 0.2.5 (Jan Rodak)
- Show referenced OVAL State (Jan Rodak)
- Parse reference in filter (Jan Rodak)
- Show OVAL Variables and referenced OVAL endpoints in report (Jan Rodak)
- Remove UUID from headings (Jan Rodak)
- Move function (Jan Rodak)
- Display in report OVAL object that references to other OVAL Objects (Jan Rodak)
- Resolve parsing of referenced OVAL Objects and OVAL Variables (Jan Rodak)
- Add OVAL Variable structure and parser (Jan Rodak)
- Rework OVAL Object and State (Jan Rodak)
- Parse mapping between OVAL var and values and propagate them (Jan Rodak)
- Remove namesapace for attributes (Jan Rodak)
- Show OVAL states in report (Jan Rodak)
- Parse attributes of elements in OVAL state and Parse all OVAL states in OVAL test (Jan Rodak)
- Show OVAL objects in report (Jan Rodak)
- Parse attributes of elements in OVAL object (Jan Rodak)
- Removing the processing of collected objects (Jan Rodak)
- Use an empty string instead of None when the text of the set-value element is empty (Jan Rodak)
- Fix deprecation warning (Jan Rodak)
- Remove product detection from the tmt plan (Jan Rodak)
- Increase vm memory (Jan Rodak)
- Add python3 dependency (Jan Rodak)
- Adjust the build of content (Jan Rodak)
- Automatic product detection to build content by CPE identifier (Jan Rodak)
- Remove whitespaces (Jan Rodak)
- Show explanation of score computation in report (Jan Rodak)
- Add explanation of score computation (Jan Rodak)
- Parse system attribute from score element (Jan Rodak)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Python Maint <python-maint@redhat.com> - 0.2.4-2
- Rebuilt for Python 3.12

* Wed Jul 05 2023 Packit <hello@packit.dev> - 0.2.4-1
- 0.2.4 (Jan Rodak)
- Rename field Result explained to Class explained (Jan Rodak)
- Add button back to top (Jan Rodak)
- Generate tooltip when hover the mouse over the OVAL operator (Jan Rodak)
- Fix persistance of checkboxes after refresh browser (Jan Rodak)
- Add functionality to buttons (Jan Rodak)
- Add buttons (Jan Rodak)
- Set logging severity from warning to info for missing fonts problem (Jan Rodak)
- Change fonts to week dependency (Jan Rodak)
- Disable scrollbar (Jan Rodak)
- Show tooltip for NOT (Jan Rodak)
- Add explanations (Jan Rodak)
- Generate tooltip (Jan Rodak)
- Set tooltip position for OVAL and CPE AL operators (Jan Rodak)
- Add new tooltip when user click on copy to clipboard (Jan Rodak)
- Rename tooltip class (Jan Rodak)
- Add new lines on end of file (Jan Rodak)
- Update eslint config (Jan Rodak)
- Implement clear button for search bar (Jan Rodak)
- Change title (Jan Rodak)
- Use the same title for the page title and report title (Jan Rodak)
- Using span element instead of link element when href is not available (Jan Rodak)
- Add non-breaking space (Jan Rodak)
- Add missing package (Jan Rodak)
- Update modules docs (Jan Rodak)
- Add documentation on how to run the test suite (Jan Rodak)
- Add usage from source (Jan Rodak)
- Add installation from source and PyPi (Jan Rodak)
- Update README (Jan Rodak)
- Sync generate_arf.sh (Jan Rodak)
- Remove execution of integration test on push to main (Jan Rodak)

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.12

* Fri Apr 14 2023 Packit <hello@packit.dev> - 0.2.3-1
- 0.2.3 (Jan Rodak)
- Determine which product use (Jan Rodak)
- Discover upstream (Jan Rodak)
- Run only smoke test in Testing Farm (Jan Rodak)
- Add weekly execution of integration test (Jan Rodak)
- Add tmt tests (Jan Rodak)
- Add tmt plan (Jan Rodak)
- Modify the smoke test to use different ARF reports (Jan Rodak)
- Add script for generation of ARF report (Jan Rodak)
- Add filter for rule id (Jan Rodak)
- Select new multi-check rules (Jan Rodak)
- Create copy of multi-check rule for every OVAL definition (Jan Rodak)
- Make method _get_applicable_cpe_ids_for_machine part of ProfileInfo and rename the method to get_list_of_cpe_platforms_that_satisfy_evaluation_target (Jan Rodak)
- Adapt input of oval_cpe_definiton in test (Jan Rodak)
- Adapt the mapping of OVAL definitions to the new OVAL definition analysis system and specify which OVAL result report is for CPE (Jan Rodak)
- Parse all OVAL definition from all OVAL result reports (Jan Rodak)
- Add parsing of OVAL refence to OVAL report (Jan Rodak)
- Load all oval reports present in ARF report (Jan Rodak)
- Fix typo in link (Jan Rodak)
- Sync tests with downstream (Jan Rodak)
- Add required parameter (Jan Rodak)
- Move unit tests from interation_tests direcory (Jan Rodak)
- Move function get_fake_args to test utils (Jan Rodak)
- Create separate job propose_downstream for EPEL8 (Jan Rodak)
- Sort chapters (Jan Rodak)
- Add manual about report content (Jan Rodak)
- Add assets (Jan Rodak)
- Fix typo (Jan Rodak)
- Add license tag (Jan Rodak)
- Add explanation of result of OVAL definition (Jan Rodak)
- Parse class of OVAL definition (Jan Rodak)
- Add tests for CPE AL (Jan Rodak)
- Fix negation of logical test (Jan Rodak)
- Add support for check-fact-ref element in CPE-AL (Jan Rodak)

* Tue Mar 28 2023 Packit <hello@packit.dev> - 0.2.2-0
- 0.2.2 (Jan Rodak)
- Clean up CI jobs titles (Evgeny Kolesnikov)
- Fix RHEL8/EPEL8 build and test integration (Evgeny Kolesnikov)
- Show message for OVAL object (Jan Rodak)
- Parse message of collected OVAL object (Jan Rodak)
- Create OvalObjectMessage (Jan Rodak)
- Create a clickable rule title to show rule detail (Jan Rodak)
- Add a copy remediation to the clipboard (Jan Rodak)
- Uderline remediation summary (Jan Rodak)
- Replace word search with filter (Jan Rodak)
- Fix compatibility issue with python3.8 in the test suite (Jan Rodak)
- Execute test suite with python3.8 and the latest python (Jan Rodak)
- Create package dependency test for centos stream 8 (Jan Rodak)
- Create copr build for rhel8 (Jan Rodak)
- Fix TypeError: 'type' object is not subscriptable coused by downgrade (Jan Rodak)
- Downgrade the minimum version of python (Jan Rodak)
- Add spec file for rhel8 (Jan Rodak)
- Fix W3601 (Jan Rodak)

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
