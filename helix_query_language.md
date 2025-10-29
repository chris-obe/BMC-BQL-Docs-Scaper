

---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/

Default language.

# Using the Query Language

This topic provides information and instructions for using the query language.

## Search expressions

The query language provides a natural mechanism for searching and processing the data model. The basic format of a search expression is: SEARCH [ in partition ] < kinds > [where clause] [traversals] [ordering] [show clause] [processing]

[ in partition ]

Used to search in a named partition.

< kinds >

Used to specify the kinds of nodes to find.

[where clause]

Used to filter the current set of nodes.

[traversals]

Used to define a traverse from one node to another in order to access attributes and relationships from related nodes.

[ordering]

Used to define a sort order for the results.

[show clause]

Used to define the information to return in the search results.

[processing]

Used to post-process the results of a search.

## Example of a query

As a simple example, the following query retrieves all Host objects where the OS is Microsoft Windows. It displays each host's name and how much RAM it has; the results are sorted by name.

The following example finds all nodes that mention Microsoft:

In this example, both the ordering and show clauses are absent. The search service therefore uses the taxonomy definitions to choose defaults. The results are ordered by the label attributes of each node kind found and the attributes to show are set according to the corresponding summary lists. (If no definitions are given in the taxonomy for a node kind, the results are not sorted and all attributes are shown.)

The following example searches the _System partition for Users:

When writing search queries, you should be aware that an unconstrained search can have a serious performance impact on the appliance. For example, SEARCH * would return details of every node in the entire datastore!

The sets resulting from searches (and traversals ) can be named and combined using set operations. This is described in Results Post Processing .

## LOOKUP expressions

Instead of performing a SEARCH , a search can be performed with a LOOKUP that simply finds one or more nodes with their node id:

An example finding a single node:

An example finding multiple nodes:

A LOOKUP cannot have a WHERE clause. It is usually used in conjunction with one or more traversals.

## Metadata LOOKUP expressions

LOOKUP is also used to retrieve a number of system metadata results:

LOOKUP version

Returns a single row of data with three columns: version number, release number, release code name

LOOKUP partitions

Returns a single column of data in which the rows list the names of the partitions within the datastore

LOOKUP partition_ids

Returns two columns of data in which the rows list the names and IDs of the partitions within the datastore

LOOKUP counts

Returns counts of nodes and relationships separated by node kind and partition

## Comments

Search queries can contain comments on lines starting // . Everything is ignored from // to the end of line.

## Literal strings

Literal strings used in search expressions can take a number of forms.

A string terminated by an unescaped ' character. Cannot include newlines.

A string terminated by an unescaped " character. Cannot include newlines.

A string terminated by an unescaped ''' character sequence. Can include newlines.

A string terminated by an unescaped """ character sequence. Can include newlines.

In normal string literals, escape characters start with backslash \ characters. Usual C-style escapes are permitted.

Strings can be 'qualified' to change their interpretation, by prefixing the string literal with a word as follows:

Backslash characters do not resolve to escape sequences.

Backslash characters do not resolve to escape sequences. Intended for use in MATCHES expressions.

Backslash characters do not resolve to escape sequences. Intended for use with filesystem paths.

Expanded into a regular expression suitable for matching a UNIX command by prefixing with '\b' and suffixing with '$' .

Expanded into a regular expression suitable for matching a Windows command by prefixing with '(?i)\b' and suffixing with '\.exe$' .

## Keywords

In this document, query language keywords appear in upper case to make them stand out. Keywords are actually case-insensitive, so they can be specified in lowercase or mixed case.

Note

All other parts of query expressions are case sensitive.

To use an identifier that clashes with a keyword, prefix it with a $ character to prevent the parser reporting a syntax error:

For backwards-compatibility, keywords can also be escaped with the ~ character. The keywords are as follows:

Logical operator when defining conditions. See Logical Operators .

Modifier defining default heading shown. See The-SHOW-Clause . Use in function result naming. See Name-binding .

Used in ORDER BY clause. See Ordering .

Used in Definition Boolean condition. See Conditions .

Changes sort order from ascending to descending. See Ordering .

Used for repeated traversals. See Traversals .

Used to 'explode' the items in the list into multiple output rows. See Explode .

Used to modify behavior with destroyed nodes, result segmentation and other characteristics. See Search-Flags-and-limits .

Used in substring and subword Boolean conditions. See Conditions .

Used in containment Boolean conditions. See Conditions . Used with STEP when performing traversals, to move from a set of nodes to a set of relationships. See Traversals .

Used in definition Boolean conditions. See Conditions .

Deprecated synonym for MATCHES .

Used to show localized column headings in queries. See The-SHOW-Clause .

Finds a single node.

Used in Boolean conditions when matching regular expressions. See Conditions .

Returns number of nodes when performing traverses. See NODECOUNT-Expressions .

Returns a list of the traversed-to nodes. See NODECOUNT-Expressions .

Used in substring and subword Boolean conditions. See Conditions . Logical operator when defining conditions. See Logical Operators .

Logical operator when defining conditions. See Logical Operators .

Used in ORDER BY clause. See Ordering .

Used with STEP when performing traversals, to move from a set of relationships to a set of nodes. See Traversals .

Used to summarize or modify the search results. See Results-after-processing .

Used to summarize or modify the search results. See Results-after-processing .

Runs a search. See .

Defines the columns to return in the search results. See The-SHOW-Clause .

Used with IN and OUT when performing traversals, to move between nodes and relationships. See Traversals .

Used in substring Boolean condition. See Conditions .

Used in subword Boolean condition. See Conditions .

Used to show the taxonomy-defined summary list in the search results. See The-SHOW-Clause .

Used to order by the taxonomy-defined label and to refer to named attribute lists. See Ordering .

Used to traverse from one node to another in order to access attributes and relationships from related nodes. See Traversals .

Filters the current set of nodes according to a Boolean condition. See Logical-and-arithmetic-expressions .

Used with the PROCESS keyword to specify the post processing function to use. See Results-after-processing . Used in function result naming. See Name-binding .

## Kind selection

A search expression must specify the kinds of nodes to search. The specification must either be a single * character, meaning to search all kinds, or a comma-separated list of node kinds. The majority of queries specify a single kind.

## Related topics

Key-expressions

Query-Language-Functions

Searching-your-data

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Key-expressions/

Default language.

# Key expressions

The WHERE , ORDER BY and SHOW clauses often use simple attribute names, as in the examples describes in the using query language section. In some cases, however, a query needs more complex specifications.

The first option is to use a 'key expression' to retrieve information from related nodes. Key expressions start with a # character.

The key expression formats are:

Traverses from the node via the roles and relationships, returning the attribute of the target node. If more than one target can be reached, returns a list of up to 10 (or an alternative limit chosen in the system options).

As explained in the previous row, but returns a 'NodeHandle' for the target node, rather than an attribute of it, useful as a function argument.

Step in to a relationship and get its attribute.

Step in to a relationship and return a 'RelationshipHandle' for it, to pass into functions.

Step out of a relationship and get the destination node's attribute.

Step out of a relationship and return the destination 'NodeHandle'.

Return the node's id in hex string format.

Returns the node's datastore partition id.

Returns the node ID in binary format.

Returns a 'NodeHandle' for the node itself, to pass into various functions.

Returns the node itself.

Applies Python format string to the attributes (which can be key expressions) in the list.

So, extending the example of finding Windows hosts, this expression shows the IP addresses of the hosts' network interfaces:

The traversal syntax permits components to be wild-carded by leaving them blank. For example, the following query shows the names of all software running on a Host, both Business Application Instances and Software Instances:

### Key expression name binding

Repeated key expressions can lead to long impenetrable search expressions. To avoid this, they can be bound to names. For example:

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Query-Language-Functions/

Default language.

# Query Language Functions

Another option for manipulating attributes is to apply functions to them. Functions are applied using the familiar parenthesis syntax:

The following topics are covered in this section:

Value manipulation IP address Node manipulation History functions System interaction Link functions

Value manipulation

IP address

Node manipulation

History functions

System interaction

Link functions

## Value manipulation

The following functions operate on normal attribute values.

abs(value)

bin(value, bins [, legend])

boolToString(value)

booleanLabel(value, true_label, false_label, other_label)

duration(start_time, end_time)

currentTime()

defaultNumber(value, default_value)

extract(value, pattern [, substitution ])

flatten(value)

fmt(format, ...)

fmt_map(format, items)

formatNumber(value, singular, plural, other)

formatQuantity(value, format)

formatTime(time_value, format)

formatUTCTime(time_value, format)

friendlyTime(time_value)

friendlyUTCTime(time_value)

friendlyDuration(duration [, friendly=1 ])

friendly_duration(duration [, friendly=1 ])

get(item, attribute [, default ])

hash(value)

int(value [, default])

join(value, separator)

leftStrip(value)

len(value)

lower(string_value)

parseTime(time_string)

parseUTCTime(time_string)

parseLocalTime(time_string)

replace(value, old, new)

recurrenceDescription(recurrence)

rightStrip(value)

single(value)

size(value)

sorted(values)

split(value [, separator ])

str(value)

strip(value)

sumValues(values)

time(time_val)

toNumber(value [, base ])

toText(value [, base [, width ] ])

unique(values)

upper(string_value)

value(item)

whenWasThat()

#### abs(value)

Returns the absolute value of an integer.

#### bin(value, bins [, legend])

Separates numeric values into 'bins', based on a list of values providing the bin boundaries, for example, a search like this:

gives results like

rs6000

1888

1024-4096

jpl64app

896

512-1024

sol10x86

288

64-512

linux-mandr-9-1

32

Less than 64

lonvmserv02

12288

4096 and more

The optional legend parameter allows the bins to be named. The list must have one more item than the bins list. For example:

rs6000

1888

1G to 4G

jpl64app

896

512M to 1G

sol10x86

288

64M to 512M

linux-mandr-9-1

32

Less than 64M

lonvmserv02

12288

More than 4G

#### boolToString(value)

Interprets its argument as a Boolean and returns "Yes" or "No".

#### booleanLabel(value, true_label, false_label, other_label)

A more advanced version of boolToString , which lets you choose which label to use for the True , False , and None cases.

#### duration(start_time, end_time)

Calculates the amount of time elapsed between the two dates and returns the result as a string of the form ' days . hours : minutes : seconds '.

#### currentTime()

Returns the number of 100 nanosecond intervals since 15 October 1582. This example query returns the hosts created in the last 7 days:

#### defaultNumber(value, default_value)

Attempts to convert the value into a number and if it is not possible returns the default value.

#### extract(value, pattern [, substitution ])

Performs a regular expression extraction. The value is matched against the pattern . If no substitution is given, returns the part of the value that matched the pattern. If substitution is given, it specifies a string including group references of the form \1 , \2 , and so on, that are filled in with the corresponding groups in the pattern. If the value does not match the pattern, returns an empty string. Strings containing backslashes must be specified with a regex qualifier, for example, regex "\1" .

#### flatten(value)

Converts a list of nested lists into a flat list. Each list item can be any data structure that is not a list. If the received value is not a list, returns a list that holds only that value.

#### fmt(format, ...)

The first argument is a Python format string, the remaining arguments are values to interpolate into it. The result is equivalent to a key expression of the form #"format"(...) , except that the arguments to the fmt() function can be the results of other functions. That is, these two expressions are equivalent:

Whereas the following expression can only be done with fmt() because it calls the len() function:

The following example shows the fmt() function used to show the results of floating point arithmetic:

#### fmt_map(format, items)

Applies a format string to all items in a list. The format argument must be a python format string with only one variable. items is the list of items to interpolate into the string. Returns a list of strings as a result.

#### formatNumber(value, singular, plural, other)

If value is 1, returns singular , if value is a number other than one, return plural with the value inserted at the mandatory %d inside it, and if value is not a number return other . e.g.

#### formatQuantity(value, format)

Takes a value (bits or bytes) and applies user friendly formatting, putting the values into KiB, Mb, and so on. The value , an int or a float is formatted according to a number of fixed format parameters. Format parameters are all literal strings. If non-numeric values such as strings or None are passed then they are returned unmodified.

The format parameters and examples are shown in the following table:

Value

Format parameter

Result

1000

"1000"

1 k

1000000

"1000"

1 M

1000

"1024"

1000

1000000

"1024"

976.6 Ki

1000

"B1000"

1 kB

1000000

"B1000"

1 MB

1000

"B1024"

1000 bytes

1000000

"B1024"

976.6 KiB

1000

"b1000"

1 kb

1000000

"b1000"

1 Mb

1000

"b1024"

1000 bits

1000000

"b1024"

976.6 Kib

1000

"bitrate"

1 kbit/s

1000000

"bitrate"

1 Mbit/s

1000

"byterate"

1 kB/s

1000000

"byterate"

1 MB/s

In the taxonomy, the attributes are not always mentioned in bits or bytes. For example: In FileSystem nodes, the unit of the size attribute is kB. Use formatQuantity(size *1024 , 'B1024') in this case.

The following example shows applying friendly formatting the raw capacity of a StoragePool:

Name

Total Raw Capacity

Size 1000

Size B1024

Pool 1

1435374714880

1.4 T

1.3 TiB

Pool 2

27686186726640

27.7 T

25.2 TiB

Pool 3

384832081920

384.8 G

358.4 GiB

Pool 4

0

0

0 bytes

#### formatTime(time_value, format)

Converts the internal time format to a string, based on the format specification, and converting into the appliance's time zone. The format is specified using Python's strftime format. For example, a search like this:

Gives results:

lonvmserv03

15 January 2009

rs6000

12 January 2009

sol10x86

13 January 2009

#### formatUTCTime(time_value, format)

Identical to formatTime , except that it does not perform timezone conversion.

#### friendlyTime(time_value)

Converts the internal time format into a human-readable string, taking into account time zones and daylight saving times, based on the appliance's time zone.

#### friendlyUTCTime(time_value)

Converts the internal time format into a human-readable string without converting the time to account for time zones and daylight saving times.

#### friendlyDuration(duration [, friendly=1 ])

Takes a duration in seconds and returns a human-readable result string, such as '3 days' or '1 month' or 'less than a minute'. The result is not intended to be precise, but to be quickly understood by a person. Note that the duration is in seconds, not the internal time format. There are 10 million internal time units per second.

If the optional friendly parameter is set to zero, the time is presented as days.hours:minutes:seconds as with the duration function.

#### friendly_duration(duration [, friendly=1 ])

A synonym for friendlyDuration.

#### get(item, attribute [, default ])

Retrieve attribute from item . If the item does not have the specified attribute, returns default if it is specified, or None if not.

#### hash(value)

Returns the MD5 hash of the specified value.

#### int(value [, default])

Converts a string form of an integer to an integer. Works on lists. Optionally supports a second argument, which if present will be used if the string cannot be converted.

#### join(value, separator)

Build a string out of a list by concatenating all the list elements with the provided separator between them.

#### leftStrip(value)

Returns the value with white space stripped from the start.

#### len(value)

Returns the length of a string or list.

#### lower(string_value)

Returns a lower-case version of a string.

#### parseTime(time_string)

Converts a date/time string into the internal format, without time zone conversion.

#### parseUTCTime(time_string)

Converts a date/time string into the internal format. Identical to parseTime .

#### parseLocalTime(time_string)

Converts a date/time string into the internal format, taking into account time zones and daylight saving times, based on the time zone of the appliance.

#### replace(value, old, new)

Modifies value , replacing all non-overlapping instances of the string old with new .

#### recurrenceDescription(recurrence)

Converts a recurrence object to a human readable string.

#### rightStrip(value)

Returns the value with white space stripped from the end.

#### single(value)

If value is a list, return just the first item of it; otherwise return the value unchanged. This is useful when following key expressions that usually return a single item, but occasionally return multiple. e.g.

#### size(value)

Returns the size of a list or string. A synonym for len() .

#### sorted(values)

Returns the sorted form of the given list.

#### split(value [, separator ])

Split a string into a list of strings. Splits on white space by default, or uses the specified separator .

#### str(value)

Converts its argument to a string.

#### strip(value)

Removes white space at the start and end of the value.

#### sumValues(values)

Sums a list of values. For example, to total the count attributes of the Software Instances related to each Host:

#### time(time_val)

Marks a number to indicate that it is a time. The values returned by functions such as currentTime and parseTime are large numbers (representing the number of 100 nanosecond intervals since 15 October 1582), which can be manipulated by other functions and compared to each other. To return them in results in a way that the UI knows that they are times, they must be annotated as times using the time function.

#### toNumber(value [, base ])

Converts a string into a number. If base is given, uses the specified base for the conversion, instead of the default base 10.

#### toText(value [, base [, width ] ])

Converts a number to a string. If base is given, the conversion uses the specified base. Only bases 8, 10 and 16 are valid. If width is given, the string is padded so that it contains at least width characters, padding with spaces on the left.

#### unique(values)

Returns a list containing the unique values from the provided list.

#### upper(string_value)

Returns an upper-case version of a string.

#### value(item)

Returns item unchanged. This is only useful to bind a non-function result to a name, as described in Name-binding .

#### whenWasThat()

Converts the internal time format to something easily readable, like '1 hour ago', '2 weeks ago', and so on.

## IP address

The following function operates on IP addresses.

inIPRange(attr, range)

#### inIPRange(attr, range)

Returns True if the IP address is in the specified range, False if not.  Where attr is an attribute or expression containing an IP address and range is an IP address range specified in the following manner:

IPv4 range: for example 192.168.1.100-105 , 192.168.1.100/24 , or 192.168.1.* .

IPv6 network prefix: for example fda8:7554:2721:a8b3::/64 .

For example:

search IPAddress where inIPRange(ip_addr, "10.1.2.*")

search IPAddress where inIPRange(ip_addr, "10.3.0.0/16")

You can also use a list attribute that contains a list of IP addresses, in which case it matches if any of the addresses in the list match the range. For example:

## Node manipulation

These functions must be passed nodes with key expressions, often just a single # to represent the current node:

destroyed(node)

hasRelationship(node, spec)

id(node)

keys(node)

kind(node)

label(node)

modified(node)

provenance(node, attribute [, show_attribute])

NODECOUNT and NODES

#### destroyed(node)

Returns True if the node has been destroyed, False if not. Returns [invalid node] if the argument is not a node. Works on lists of nodes as well, returning a list of boolean values. (See the section on Search-Flags-and-limits that permit searching destroyed nodes.)

#### hasRelationship(node, spec)

Takes a node and a traversal specification. Returns True if the node has at least one relationship matching the specification; False if not. Works on lists of nodes as well.

#### id(node)

DEPRECATED function to return a node id in string form. Use #id to return a node's id.

#### keys(node)

Returns a list of the keys set on the node. Returns [invalid node] if the argument is not a node. Works on lists of nodes as well, returning a list of lists of keys.

#### kind(node)

Returns the kind of the node. Returns [invalid node] if the argument is not a node. Works on lists of nodes as well, returning a list of kinds.

#### label(node)

Returns the node's label, as defined in the taxonomy. Works on lists of nodes as well, returning a list of labels.

#### modified(node)

Returns the node's last modified time in the internal numeric format, this includes any modification, including relationships to the node. The modified() function works on lists of nodes as well, returning a list of times.

Modification times and host nodes

At the end of each discovery run, the automatic grouping feature considers all the Hosts, and builds a new set of automatic grouping relationships. It commits one big transaction that adjusts all the relationships to all Hosts, so every Host node usually has the same modification time.

#### provenance(node, attribute [, show_attribute])

Follows provenance relationships from the node, finding the evidence node that provided the specified attribute. If the show_attribute is given, returns the specified attribute of the evidence node; if not, returns a handle to the node itself.

#### NODECOUNT and NODES

In addition to the functions described in the previous section, the NODECOUNT and NODES keywords, defined in Traversals , behave like functions in some respects.

## History functions

The following history-related functions are currently available.

creationTime(node)

createdDuring(node, start, end)

destroyedDuring(node, start, end)

destructionTime(node)

eventOccurred(node, start, end)

#### creationTime(node)

Returns the number of 100 nanosecond intervals between 15 October 1582 and the time the node was created. Also works on lists of nodes.

#### createdDuring(node, start, end)

Returns true if the node was created during the time range specified with start and end. For example, to find all the application instances created between 1st July and 10th July 2008.

#### destroyedDuring(node, start, end)

Returns true if the node was destroyed during the time range specified with start and end. To find all the application instances destroyed between 1st July and 10th July 2008:

#### destructionTime(node)

Returns the time the node was destroyed in the internal time format. If the node is not destroyed, returns 0. Works on lists of nodes as well, returning a list of destruction times.

#### eventOccurred(node, start, end)

Takes a node and two times in the internal format. Returns True if the node was modified between the specified times; False if not. Works on lists of nodes as well. Returns [invalid time] if the times are invalid.

### Specialist history functions

The following history functions can be used for specialist purposes:

newInAttr(node, attr, timeA, timeB)

attrSpread(node, attr, timeA, timeB)

newInAttrSpread(node, attr, timeA, timeB, timeC)

historySubset(nh, timeA, timeB, attrs, rels)

#### newInAttr(node, attr, timeA, timeB)

Retrieves the node's specified attribute at the two times. The attribute is expected to contain a list. Returns a list containing all items that were present in the list at timeB that were not present at timeA .

#### attrSpread(node, attr, timeA, timeB)

Returns a list containing all unique values that the attribute has had between the two times.

#### newInAttrSpread(node, attr, timeA, timeB, timeC)

A cross between newInAttr and attrSpread. Returns a list of values for the attribute that existed at any time between timeB and timeC , but which did not exist at any time between timeA and timeB .

#### historySubset(nh, timeA, timeB, attrs, rels)

Reports on a subset of the node history between the two times. attrs is a list of attribute names to report; rels is a list of colon-separated relationship specifications to report, only single-hop relationships are supported. For example, the following query will show changes to os_type , os_version , and hosted SoftwareInstances for a collections of Hosts:

See also the post-processing function displayHistory in Results-after-processing .

## System interaction

These functions allow access to other aspects of the BMC Discovery system.

fullFoundationName(username)

getOption(key)

#### fullFoundationName(username)

Returns the full name of the user with the given user name or None if no such user exists.

#### getOption(key)

Returns the value of the system option key .

## Link functions

When search results are shown in the UI, each cell in the result table is usually a link to the node corresponding to the result row. These functions allow other links to be specified:

nodeLink(link, value)

queryLink(link, value)

#### nodeLink(link, value)

link is a node id or node reference, for example the result of a key expression; value is the value to display in the UI and to be used in exports. For example, to create a table listing Software Instances and their Hosts, with links from the host names to the Host nodes:

#### queryLink(link, value)

link is a search query to execute; value is the value to display in the UI and to be used in exports.

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Logical-and-arithmetic-expressions/

Default language.

# Logical and arithmetic expressions

Logical and arithmetic expressions can be used in SHOW clauses and WHERE clauses.

## Truth

In WHERE clauses, the following values are considered False:

Boolean False

Number zero

Empty string

Empty list

None (for example, missing attribute)

All other values are considered True. This allows simple WHERE clauses that choose only useful values. For example, to find all Software Instance nodes with a populated version:

## Expressions

The following logical and arithmetic expressions are supported:

Equality

Inequality

Comparison

a > b a >= b a < b a <= b

Arithmetic

a + b a - b a * b a / b

Subwords

a HAS SUBWORD b Case-insensitive subword or phrase test. a is split into a word list using non-alphanumeric characters to identify the word boundaries.

For a single word search, the condition is true if b is in the list of split words.

For a multi-word search:

To find a number of words in the text, disregarding the word order, enclose the words with quotation marks, for example: os_type has subword "Red Hat Linux" This condition is true if all the words "Red", "Hat", and "Linux" are found as subwords of the full text, not limiting results to the exact phrase match. For example, if os_type is "Red Hat Enterprise Linux", the search in the previous example returns true.

To find a number of words in the text, disregarding the word order, enclose the words with quotation marks, for example:

This condition is true if all the words "Red", "Hat", and "Linux" are found as subwords of the full text, not limiting results to the exact phrase match. For example, if os_type is "Red Hat Enterprise Linux", the search in the previous example returns true.

To find an exact phrase in the text, taking into account the word order, enclose the phrase in square brackets, like in the following example: os_type has subword ["Red Hat Linux"] This condition is true if the exact phrase is found as a subphrase of the full text, matching the word order. For example, if os_type is "Red Hat Enterprise Linux", the condition in the previous example returns false.

To find an exact phrase in the text, taking into account the word order, enclose the phrase in square brackets, like in the following example:

This condition is true if the exact phrase is found as a subphrase of the full text, matching the word order. For example, if os_type is "Red Hat Enterprise Linux", the condition in the previous example returns false.

When used in a WHERE clause, HAS SUBWORD uses the full text indexes maintained by the datastore. It is one of the most efficient ways to find nodes.

Substrings

a HAS SUBSTRING b Case-insensitive substring test. Where possible HAS SUBSTRING uses the full text indexes maintained in the data store, but it is always less efficient than HAS SUBWORD .

Regular expression match

a MATCHES b a LIKE b The condition is True if a matches regular expression b . LIKE is a deprecated synonym of MATCHES . MATCHES cannot often use the datastore indexes, and is therefore by far the slowest mechanism for finding nodes. If at all possible queries should use HAS SUBWORD instead of MATCHES .

Containment

a IN b a NOT IN b The condition is True if a is/is not in b , where b is a list.

Containment

a IN [b, c, d...] a NOT IN [b, c, d...] The condition is True if a is/is not in the specified list.

Definition

a IS DEFINED a IS NOT DEFINED The condition is True if the node has an attribute a (with any value).

Inverse

NOT a True if a is considered False; False if it is considered True.

And

a AND b Considered True if both a and b are considered True. If a is considered True, the value of the expression is b ; if a is considered False, the value of the expression is a .

Or

a OR b Considered True if either a is considered True or b is considered True. If a is considered True, the value of the expression is a ; otherwise the value of the expression is b .

## Precedence

Operator precedence works as you would expect. Parentheses ( and ) are used to explicitly group operations. Otherwise, in arithmetic expressions, * and / take precedence over + and - . In logical expressions, OR has lowest precedence, followed by AND , followed by NOT , followed by all the other operators. i.e. this expression

is equivalent to

## Logical expressions in SHOW clauses

Logical expressions can be used in SHOW clauses. To do so, they must be enclosed in parentheses, e.g.

The behavior of AND and OR in returning one of their input parameters can be useful in handling missing attributes, to avoid output of "None" when an attribute is not available, for example:

## Logical expression name binding

Logical expressions can be bound to names. For example:

## Using a regular expression

The MATCHES condition enables you to search by matching against a regular expression (or regex ), a pattern that matches various text strings. For example, A[0-9]+ matches any string that consists of the letter A followed by one or more digits.

Regular expressions have a defined syntax that enables you to define complex matching patterns. BMC Discovery uses the Python implementation; for full syntax and details of use, consult the Python documentation. For more information, see the Python documentation .

The following table lists a few of the matching characters that you can use when constructing regular expressions. An ordinary character, or a sequence of characters, matches that character or string.

## Related topics

Using-the-Query-Language

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Name-binding/

Default language.

# Name binding

It is sometimes necessary to use the result of calling a function more than once, for example using a result as part of a WHERE clause, and then using the value in a SHOW clause. To avoid repeated function evaluation, the result of a function can be bound to a name using a WITH clause. The result can then be referred to later by name, prefixed with an @ character. For example:

Only function results can be bound to names in this way. It is not possible to directly use a logical or arithmetic expression. To do so, you can use the value() function as a wrapper around the expression:

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Traversals/

Default language.

# Traversals

A SEARCH expression creates a set of nodes, and a LOOKUP makes a set with just one node in it. With that set, a query can TRAVERSE from each of the nodes to a new set of related nodes. The format of a TRAVERSE expression is

The WHERE clause allows the new set to be further filtered. For example, to find all software instances that are running on Linux hosts:

As with key expressions, elements of the traversal can be omitted as a wildcard mechanism. All matching relationships are followed, so this example finds software running on Linux hosts, and virtual machine software containing the hosts:

Adding some filtering:

The attributes that are accessed in the TRAVERSE WHERE clause are attributes of the nodes that have been traversed to, not attributes of the original nodes. The original nodes have been discarded from the set.

Traversals can be chained, so we can now find any business application instances related to the software instances:

At each stage, the result of a traversal is a set, so each node appears only once in the set, even if it is reached via relationships from more than one node.

A TRAVERSE clause performs one single traverse from each node in the current set. Sometimes it is useful to repeatedly traverse to find all the nodes that can be reached via particular relationships, using an EXPAND clause. This is useful for finding all applications that depend on a particular other application, for example:

The set now contains the original nodes, plus all the nodes that depend upon them, via any number of intermediate dependencies. The EXPAND keeps performing traversals until no more nodes are found. The EXPAND always keeps the original set. If you want to EXPAND but not keep the original set, use a TRAVERSE followed by an EXPAND :

Just like a TRAVERSE clause, an EXPAND can have a WHERE clause. The filtering of the WHERE clause happens once the EXPAND has completed, not on every traversal iteration (since if it did it every iteration, it might never complete).

TRAVERSE and EXPAND move from one set of nodes to another set of nodes. Sometimes, you want to stop off at a relationship along the way. This is achieved with STEP IN, which replaces the set of nodes with a set of relationships. Given a set of relationships, you can STEP OUT to another set of nodes. To find critical Dependency relationships:

To find the BusinessApplicationInstances that have a critical dependency to the ones matched in the WHERE clause:

To find a relationship between 2 named nodes:

To find all the relationships between 2 named nodes:

### Named and filtered sub-traversals

To see the types of all the SoftwareInstances running on each Host, you can use the following traversal:

You can also use a named traversal to do the same thing:

You can filter the results using a WHERE clause:

An example of how these can be used is to find named attributes on Detail nodes. For example, a standard TKU pattern creates "LPAR Resource" Detail nodes with additional details about LPAR allocations for AIX machines. One of the attributes on those Details is entitled_capacity. Using a key expression to find it:

As there are other, completely different Detail nodes related to those Hosts which do not have an entitled_capacity attribute, so they show as "None". For example:

Using a named traversal, we can filter out the non-matching nodes.

For example:

The last host in the list had five Nones before, meaning it had five non-matching Detail nodes, and no LPAR Resource Detail. Now it reports "Not set", because there was nothing matching.

Similarly, when Software Instances are modeled running on a Cluster, they are given "ClusteredSoftware" relationships to each of the Host nodes that are in the cluster, to efficiently answer the common question of which software is on which hosts. When the Cluster node represents a fail-over cluster, one Host is "active" and the others are not. BMC Discovery sets an "active" attribute on the relationship leading to the Host that was most recently seen to be the active one. Because the data is on the relationship, it can be tricky to access. Using a simple key expression to access the Host for SoftwareInstances in fail-over clusters:

Each SI reports two hosts, because these are fail-over clusters of two hosts. We cannot see which one is active.

Using a traversal expression to access the relationship and the target node:

We see just the active Host for each SI.

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/NODECOUNT-Expressions/

Default language.

# NODECOUNT Expressions

Sometimes it is useful to filter, sort, or show the number of nodes related to each node in the set. This is achieved with a NODECOUNT expression. It behaves like a function, except that its arguments are a traversal clause. To show the number of dependencies of each Business Application Instance:

NODECOUNT accepts all the traversal expressions described in the previous section, including chaining and where clauses.

NODECOUNT is the correct way to filter based on properties of related nodes, rather than using a key expression in a WHERE clause. The following is a way to find all Linux Hosts running products from the Apache foundation, for example:

Similar to NODECOUNT , the NODES keyword performs a traversal and returns a list of the traversed-to nodes. It is only used for internal purposes since, in general, lists of nodes cannot be handled in the search service.

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Search-Flags-and-limits/

Default language.

# Search Flags and limits

Certain aspects of search behavior can be modified by setting 'flags' for the search. Flags are applied with the flags keyword, or in square brackets and affect the whole search:

Flags can also be applied to traversals, in which case they apply to just the traversal:

## Flags

The following flags are available:

Flags include_destroyed exclude_current no_segment find_relationships suppress_default_links Limits Flags and limits

Flags include_destroyed exclude_current no_segment find_relationships suppress_default_links

include_destroyed exclude_current no_segment find_relationships suppress_default_links

include_destroyed

exclude_current

no_segment

find_relationships

suppress_default_links

Limits

Flags and limits

#### include_destroyed

Normally, nodes and relationships that are marked as destroyed are excluded from searches and traversals. The include_destroyed flag means that destroyed nodes and relationships are included.

#### exclude_current

With include_destroyed , searches involve both current and destroyed nodes; with the additional exclude_current flag, current nodes are excluded. exclude_current only makes sense when used in conjunction with include_destroyed , otherwise everything is excluded.

#### no_segment

Normally, a search that finds multiple target nodes segments its results so that each node kind is in a separate result set. no_segment prevents the segmentation, meaning the results are in just one set. This is generally only useful when the node kinds are similar in some way, otherwise it is impossible to define a suitable SHOW clause for the combined results.

#### find_relationships

Searches normally find nodes with the specified kinds. The find_relationships flag causes searches to find relationships instead.

#### suppress_default_links

When presented in the UI, search results are normally presented so that each row is a link to the node from which the data came. The suppress_default_links flag removes these default links.

## Limits

A limit on the number of results returned can also be specified. Limits are applied using a square bracket syntax. To return five matching hosts from a search:

## Flags and limits

Limits and flags can be combined. For example, the following query returns no more than five matching hosts, and as exclude_current is used in conjunction with include_destroyed , it only returns destroyed hosts:

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Ordering/

Default language.

# Ordering

After processing a SEARCH or LOOKUP and any traversals, the set of nodes is in an arbitrary order. If the query expression contains an ORDER BY clause, the set is sorted according to the clause. The clause is a comma separated list of attributes (or key expressions, function calls, and so on). The set is sorted according to the first attribute in the list; those that are identical by the first attribute are further sorted according to the second attribute in the list, and so on.

Sorting is normally in ascending order; the order can be reversed with the DESC modifier:

If the search expression does not have an ORDER BY clause, it is returned in an arbitrary order unless the taxonomy is consulted for the SHOW clause. For more information, see the following section. In that case, the set is sorted by the taxonomy-defined label attribute.

## Named taxonomy attribute lists

The taxonomy supports multiple named attribute lists. These can be referred to in queries using the TAXONOMY keyword. For example:

or

Comments (1)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/The-SHOW-Clause/

Default language.

# The SHOW Clause

The SHOW clause contains a list of columns to return in the search results. The clause is a comma separated list of attribute names, key expressions, functions or other expressions. For some reports, it is useful to set headings for the columns. By default, the heading for a column is the name of the attribute in that column, or a simple string describing how the value was arrived at. The default heading can be overridden with the AS modifier:

If the SHOW clause is absent, the columns are set according to the summary list as defined in the taxonomy. If the SHOW clause is a single * character, the columns are set to the field order defined in the taxonomy. In both of those cases, if there is no entry in the taxonomy for the node kinds, no columns are set, and results can not be retrieved (although the nodes themselves can still be accessed).

To show the taxonomy-defined summary list defined plus some other attributes, use the SUMMARY keyword in a SHOW clause. This query shows the OS of a Host, followed by the normal taxonomy summary:

If columns are not named with AS , the columns are named using information from the taxonomy, as long as the locale is known. Searches performed through the UI take the locale from the user's profile information. In other cases, such as exports, there is no default locale. The locale can be specified in the query:

If the locale is not known, or is is specified as the empty string, the column headings are based on the attribute names in the SHOW clause.

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Explode/

Default language.

# Explode

Normally, if an attribute contains a list, or a key expression traversal that leads to multiple nodes, all items in the list appear in a single cell in the results. Sometimes, particularly when exporting data to other systems, it can be useful instead to 'explode' the items in the list into multiple output rows. The result is similar to the result of a join in a relational database. This query produces a table of network interfaces with one fully-qualified domain name per row:

When exploding an entry, one row is created for each item in the exploded list; if the exploded list is empty, no rows are created.

A common requirement when exporting data for import into another system is to extract the node identifiers for all nodes related to a set of nodes, so the graph structure can be reconstructed. This can be achieved by exploding the related node identifiers. This query produces a table mapping Host node ids to all the Software Instances running on them:

Key expression traversals leading to multiple nodes can be limited in the system settings so that not all target nodes are used (although by default there is no limit). When exploded, key expressions have no traversal limit.

All key expressions with the same traversal specifications are handled as a group, meaning that multiple attributes can be selected, for example:

The result has one row per software instance. Even though the second key expression is not explicitly exploded, it is implicitly exploded since it shares the traversal with the exploded attribute.

This sort of implicit explode is only performed during normal result retrieval. Using PROCESSWITH to filter a search in post-processing accesses values without the context of retrieving complete rows, so implicit explodes do not take effect. This does not work:

The PROCESSWITH accesses column 1 (the instance) without also accessing column 0, meaning that the explode does not take effect. Rather than explicitly exploding the column to be filtered, it is much more efficient to use a traversal expression to choose only the selected nodes in the first place:

## Multiple Explodes

You should not use explode on more than one independent attribute or relationship traversal. If you do so, all possible combinations of the attribute values are exploded. This can produce very large datasets and can impact performance considerably.

For example, an attempt to see Hosts with all their directly running Software Instances and simultaneously all their IP addresses would be a mistake:

If a Host had 10 Software Instances and 5 IP addresses, that one Host would produce 50 rows of output. Across all Hosts, that query could easily generate many millions of rows of output.

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Results-after-processing/

Default language.

# Results after processing

After a query has completed, resulting in one or more sets of nodes, the set can be post-processed to summarize the results or otherwise modify them. This is achieved using a PROCESSWITH clause. (For backwards compatibility, PROCESSWITH can be specified as two words PROCESS WITH .)

Optional parameters

In the following example, some function parameters are shown with a value, such as min=0. This indicates that the parameters are optional, and the values are the default used if values are not provided. The key=value syntax is not part of the search syntax. Parameters must always be provided as plain values or missed out to use the defaults.

Post-processing functions can be chained together in a comma-separated list, in which case they are applied in turn, each taking the output of the previous one. For example, the following query follows from all ssh processes to processes they are communicating with:

After a search, you can immediately refine it.

@ number refers to columns in the first search, as in current refine searches. Remember that column index starts with 0. It is very rare for this kind of refine search to be necessary. Normally, the same results are obtained more efficiently by simply performing the where clause directly in the search, avoiding the PROCESSWITH altogether.

The following topics are covered in this section:

Named node sets and set operations Data manipulation functions Provenance functions Network connection functions Chart-specific functions Related topics

Named node sets and set operations

Data manipulation functions

Provenance functions

Network connection functions

Chart-specific functions

Related topics

## Named node sets and set operations

Sets resulting from searches and traversals can be given names, and then combined with set operations. You name the node set using the AS keyword. The location in which you do this is important. It must appear after the node kind, or after the traversal if one is used in the SEARCH query. For example, to find Windows hosts running Oracle products:

Valid operators for the sets are

Intersection of sets.

Union of sets.

- (minus sign)

Negative intersection.

Many post-processing functions do not create node sets

These set operations work only on sets of nodes. Many of the post-processing functions described in the following section return results in which the rows do not correspond directly with nodes. Attempting to use such post-processed results in set manipulation operations leads to an error.

## Data manipulation functions

The following functions manipulate data:

#### bucket(interval, min=0, max=0)

Separates data into 'buckets' representing ranges of values present. It looks at the first attribute selected with the SHOW clause, which should be either a number or a date. It starts by dividing the data into buckets with 'width' specified by interval . i.e. with an interval of 10, the first bucket contains the values between 0 and 10, the next between 10 and 20, and so on. The result then contains one row for each bucket, with two columns showing the bucket value and the number of input values in the bucket.

If provided, min and max specify the minimum and maximum number of buckets. If the number of buckets based on the interval is outside those boundaries, the interval is divided or multiplied by two until it fits. If used to group dates the interval is assumed to be in seconds. This function is mostly used to build charts.

#### unique(sort=0)

The unique function takes the rows of output from the search, and returns each unique row just once.

If the optional sort argument is set to 1, the result rows are sorted; if set to zero or not provided, the rows are output in the same order they appeared in the original results, with duplicates removed.

#### countUnique(show_total_count=1, show_node_count=1, sort=1, set_headings=None, ignore_none=1)

The countUnique function can be used, for example, to produce a summary of discovered processes:

It converts the search results into a summary where each row contains a command, arguments pair and count of how many times that pair appears.

When show_total_count and show_node_count are both 1 and a single list attribute is provided in the SHOW clause, countUnique considers the individual items in the lists and shows two counts. The first count is the total number of times the item appears; the second count is the number of different nodes in which the item appears. The first count will be a larger number if an item appears more than once in a list. If a non-list attribute is provided in the SHOW clause, both counts will be the same.

When show_total_count is 1 and show_node_count is 0, the function behaves as described above, but only the total count is provided. **

When show_total_count is 0 and show_node_count is 1, the function simply counts the number of nodes that contain each distinct value. List attributes are not treated in any special way, so it counts the number of distinct lists.

The sort parameter has no effect. It is retained for compatibility with earlier releases. The results are always sorted with the highest count first.

If set_headings is provided, it contains a list of strings to use as the headings for the count columns added to the result, overriding the default headings. The list must have the correct number of items corresponding for the number of columns (1 or 2 depending on the show parameters). These headings are added after the existing headings based on the search show clause.

By default, values that are None are ignored; if ignore_none is set to zero, None values are counted in the same way as other values.

#### displayHistory(start, end, attr_count)

The displayHistory function explodes a result set with history information.

The three arguments are the start date, the end date and the number of attributes to leave as is. By default the end date is now and the attribute count is 1 so this invocation could be simplified as:

This example returns a result set with one line for every change in the history of the attributes name, ram and processor, detailing on each line the date it happened, and the attribute name and the attribute value before and after the change.

## Provenance functions

These functions analyze provenance information:

#### provenanceDetails(friendly_time=0)

provenanceDetails takes all of the attributes selected in the SHOW clause and finds the provenance information for them. For each attribute it shows a row in the output containing the source node label, the attribute name, the attribute value, the time the attribute was last confirmed, and the label of the evidence node.

If the optional friendly_time argument is set to 1, the times are converted to strings; if set to 0 or not provided, times are returned in the internal time format.

#### provenanceFailures(friendly_time=0)

provenanceFailures is currently only supported for Host nodes. For each Host, it traverses to find the most recent DiscoveryAccess . It then finds the provenance information for each of the attributes in the SHOW clause. The output consists of one row for each attribute that was not confirmed in the most recent DiscoveryAccess . The rows contain the label of the Host node, the attribute name, the attribute value, the label of the evidence node used to set the attribute, the time the value was confirmed, and the time of the most recent DiscoveryAccess .

If the optional friendly_time argument is set to 1, the times are converted to strings; if set to 0 or not provided, times are returned in the internal time format.

## Network connection functions

These functions analyze network connection data:

#### communicationForProcesses(targets=3, show="SUMMARY")

Given an input of DiscoveredProcesses , returns a list of node sets which varies depending on the value of targets:

targets = 1

return DiscoveredNetworkConnections

targets = 2

return DiscoveredListeningPorts

targets = 3

return both

Returns network connections and listening ports that tie up with the given set of processes. (For example, the network connection or listening port comes from the same discovery access as the process, and the process ids match.)

The show clause determines which attributes on the nodes are returned in tabular results. The same show clause is used for both node kinds.

The result of this function is useful for feeding in to the localToRemote or communicationToRemoteHost functions.

#### processesForCommunication(show="SUMMARY")

The input must contain DiscoveredNetworkConnections or DiscoveredListeningPorts or both. Returns a node set of DiscoveredProcesses .

Returns processes that tie up with the given network connections and listening ports. (For example, the processes come from the same discovery access as the connections and ports, and the process ids match.)

The show clause determines which attributes on the nodes are returned in tabular results.

#### localToRemote(targets=15, show="SUMMARY")

The input must contain DiscoveredNetworkConnections or DiscoveredListeningPorts, or both. Returns nodes corresponding to the 'other end' of the input communication information. The results depend upon the targets specification. targets is a 'bit mask' formed by adding together the numbers corresponding to the required results:

targets

result

1

remote DiscoveredNetworkConnections

2

remote DiscoveredListeningPorts

4

in-machine DiscoveredNetworkConnections

8

in-machine DiscoveredListeningPorts

The function distinguishes between 'remote' connections that are on different computers to the source information and 'in-machine' connections that are communication from one process to another on a single computer.

DiscoveredNetworkConnection nodes can be used to find both target DiscoveredNetworkConnection and DiscoveredListeningPort nodes.

DiscoveredListeningPort nodes can only be used to find target DiscoveredNetworkConnection nodes.

In all cases, only network connections and listening ports found during the most recent complete DiscoveryAccess are considered, meaning that only 'current' data is used.

It is not an error to, for example, pass in only DiscoveredListeningPorts and set targets to 2. In this instance, an empty list results.

The show clause determines which attributes on the nodes are returned in tabular results. The same show clause is used for both node kinds.

The result of this function is useful for feeding in to the processesForCommunication function.

#### hostToHostCommunication(show="SUMMARY")

Given a set of Host nodes, returns a set of Hosts that are communicating with those hosts, according to observed network connections.

A host is considered to be communicating with another if there is a network connection from either host to the other, according to the remote IP address on the network connection and the IP addresses of the host.

The show clause determines which attributes on the nodes are returned in tabular results.

#### communicationToRemoteHost(show="SUMMARY")

Given a list of node sets, which must contain DiscoveredNetworkConnections or DiscoveredListeningPorts (or both), return a set of Host nodes that are communicating.

A Host is returned if one of its IPs matches one of the remote IP addresses of one of the network connections, or if it has a network connection with a remote IP address and port that matches one of the listening ports.

The show clause determines which attributes on the nodes are returned in tabular results.

#### hostToRemoteCommunication(show="SUMMARY")

Given a set of Host nodes, returns a list of DiscoveredNetworkConnections and DiscoveredListeningPorts that are communicating with the hosts. Network connections are returned if their remote IP address corresponds to an IP address of one of the hosts, and listening ports are returned if a network connection on one of the hosts contains a remote IP address and the port matches the listening port.

Only network connections and listening ports found during the most recent complete DiscoveryAccess are considered, meaning that only 'current' data is used.

The show clause determines which attributes on the nodes are returned in tabular results.

The result of this function is useful for feeding in to the processesForCommunication function.

#### communicatingSIs(show="SUMMARY")

Given a set of SoftwareInstance nodes, returns a set of the SoftwareInstance nodes with which they are communicating. This function is equivalent to a traversal from SoftwareInstance to DiscoveredProcess , then a chain of communicationForProcesses , localToRemote , processesForCommunication , followed by a traversal from DiscoveredProcess back to SoftwareInstance .

In BMC Discovery version 8.2.01 and later, communicatingSIs returns SoftwareInstance nodes corresponding to both remote and in-machine communication links. Earlier versions only returned SoftwareInstance nodes on remote computers.

#### connectionsToUnseen

Takes a set of DiscoveredNetworkConnection nodes, and filters it to include only those ones that represent connections to addresses that have not been seen on IPAddress nodes present in the system. That is, it returns network connections to devices that have not been scanned.

#### networkConnectionInfo

Takes a set of DiscoveredNetworkConnection nodes and produces a summary of information about each one. Each row contains the name of the "local" Host, the associated local process command and arguments, port and IP address information for the connection, the remote command and arguments, and the remote host name. Not all of the information is always available (for example, if the remote side of the connection had not been scanned, or if insufficient discovery permission meant ports were not associated with processes).

networkConnectionInfo takes four optional list parameters to modify the attributes shown for Hosts and DiscoveredProcesses. The first two parameters specify the attributes to show on Host nodes and the headings to use for those columns; the second two parameters specify the attributes to show on DiscoveredProcess nodes and the headings to use for those. The number of headings must match the number of attributes shown for each node kind. In both cases, the attributes and headings are used twice, once for the local end of the network connection, and once for the remote end. The headings are prefixed "Local" and "Remote" as appropriate.

The default settings are equivalent to networkConnectionInfo(["name"], ["host name"], ["cmd", "args"], ["command", "arguments"]) . It is valid to use key expressions in the attribute lists, so attributes from nodes related to the hosts or processes can be displayed.

#### siCommunicationSummary

Takes a set of SoftwareInstance nodes and produces a summary with one row for each observed network connection, treating the input Software Instance nodes as the local end. Each row contains the local Host and Software Instance, local and remote IP address and port, remote Software Instance and remote Host. Values for the remote end might not be available if the remote host was not scanned, or if the connection could not be associated with a particular Software Instance.

Like networkConnectionInfo , siCommunicationSummary takes four optional list parameters to modify the attributes shown for Hosts and Software Instances. The default is equivalent to siCommunicationSummary(["name"], ["host name"], ["name"], ["SoftwareInstance"]) . Key expressions are valid in the attribute lists, so attributes from nodes related to the Hosts or Software Instances can be shown.

#### hostConnectionSummary

Takes a set of Host nodes and produces a summary with one row for each observed network connection, treating the input Host nodes as the local end. Each row contains the local Host, local and remote IP address and port, local and remote process using that remote connection (if available), and remote Host. The remote Host might not be available if it was not scanned, or if the connection could not be associated with a particular Host.

## Chart-specific functions

These functions are only useful as input to charts:

#### timeSeries(column_count = 20, how_far_back = 0)

This function transforms a list of result sets with two dates into a result set of counts. An example usage is to graph the count of hosts over time. column_count determines how many data points will be present in the output, how_far_back is a time — the function will drop anything in the given set older that this date.

The function assumes that the first two columns in the passed set are dates and if another column is present returns one data set per possible value, somewhat similar to countUnique.

This function returns multiple result sets, one with a legend whose metadata dictionary contains an isLegend key. If there are more than two columns in the sources sets it returns one result set per unique value of this column:

The result set title is set to the string version of the value.

value in the metadata is the original CORBA any containing of the split value.

index in the metadata preserves the order in which the split values were found in the source nodeset.

If there are only two columns, only two result sets are returned: the legend and a list of counts, and no metadata is set. For example:

## Related topics

Using-the-Query-Language

Comments (0)


---

# Source: https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/A-Note-on-Performance/

Default language.

# A Note on Performance

There are often several ways to write a query that produces a required output report. Writing queries in different ways can sometimes cause enormous differences in query performance, so this section provides some hints on how to write queries so they are as efficient as possible.

The following topics are covered in this section:

Use of indexes WHERE clause ordering Filtering on related nodes Default ordering

Use of indexes WHERE clause ordering Filtering on related nodes Default ordering

Use of indexes

WHERE clause ordering

Filtering on related nodes

Default ordering

### Use of indexes

Wherever possible, use HAS SUBWORD rather than MATCHES / LIKE or HAS SUBSTRING so the datastore indexes are used. The full text index is very good at finding words and phrases.

### WHERE clause ordering

In WHERE clauses containing AND expressions, order the parts so that the most restrictive condition comes first, except that it is always better to use a HAS SUBWORD condition in preference to other kinds. This reduces the search space as soon as possible.

### Filtering on related nodes

To filter nodes by characteristics of related nodes, it is better to find the related nodes, then traverse to the required nodes. For example, to find Hosts in London, this query finds the London location in the index then uses a traversal so it directly and quickly finds the required Hosts:

This query starts by building a set of all Host nodes, then checks the location of each one, which is much slower:

This final version also builds a set of all Hosts and checks the location of each one, but in this case it fails when encountering Hosts in more than one location, as well as being inefficient. Queries like this should never be used:

### Default ordering

By default, queries with no SHOW clause are ordered by the label value defined in the taxonomy. If the data is to be exported to an external system that does not care about order, the time spent retrieving data to sort can be avoided by specifying ORDER BY "" .

Comments (0)
