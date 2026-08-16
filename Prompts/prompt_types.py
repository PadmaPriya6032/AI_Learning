from logging import root

from openai import OpenAI
from API_Token.API_Token import method1
import base64


api_token = method1()  # Call method1 to set the API key and retrieve it
client = OpenAI(api_key=api_token)  # Use the retrieved API key to create

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role":"system","content":prompt}
        ],
        temperature=0.0
    )

    return response.choices[0].message.content

def zeroshot():
    prompt = """
    You are a Senior QA Engineer.

    Generate functional test cases for a banking application's fund transfer feature.

    Requirements:
    - User can transfer money between accounts.
    - Daily transfer limit is ₹100000.
    - Beneficiary must be registered.
    - OTP verification is mandatory.

    Generate positive and negative test cases in a table.
    """

    print(ask_llm(prompt))

def one_shot():
    prompt = """
    You are a Senior Network QA Engineer.

    Generate 15 test cases for validating a Cisco router's DHCP configuration.

    Cover

    - Functional
    - Negative
    - Boundary
    - Security scenarios
    """

    print(ask_llm(prompt))

def few_shot():
    prompt = """
    Example 1

    Requirement:
    Ping Verification

    Output

    - Ping succeeds
    - TTL verified
    - Packet loss <1%

    ----------------------------

    Example 2

    Requirement:
    Firewall Rule Validation

    Output

    - Allowed traffic passes
    - Blocked traffic denied
    - Logs generated

    ----------------------------

    Now create test cases for

    Requirement

    OSPF Neighbor Formation
    """

    print(ask_llm(prompt))

def role_prompt():
    prompt = """
    You are a Cisco CCIE certified QA Architect.

    Design comprehensive testing scenarios for

    BGP Route Advertisement.

    Include

    - Positive
    - Failover
    - Recovery
    - Load Testing
    """
    print(ask_llm(prompt))


def Instruction_prompt():
    prompt = """
    Generate networking QA test cases.

    Instructions

    Use markdown table.

    Columns

    Test ID
    Scenario
    Steps
    Expected Result
    Priority

    Feature

    VPN Connectivity
    """

    print(ask_llm(prompt))

def contextual_prompt():
    prompt = """
    Context

    Company uses

    Cisco Routers

    Cisco Switches

    Fortinet Firewall

    Requirement

    QA engineer needs regression testing after firmware upgrade.

    Generate regression test suite.
    """

    print(ask_llm(prompt))

def chain_of_thoughts():
    prompt = """
    Think step by step.

    Requirement

    Verify OSPF routing after reboot.

    Reason through

    1. Preconditions

    2. Network topology

    3. Test execution

    4. Validation

    5. Expected outcome

    Finally generate detailed test cases.
    """

    print(ask_llm(prompt))

def tree_of_thoughts():
    prompt = """
    Evaluate three different approaches to test

    VPN Connectivity.

    Approach A

    Functional Testing

    Approach B

    Security Testing

    Approach C

    Performance Testing

    Compare all approaches and recommend best strategy.
    """

    print(ask_llm(prompt))

def persona_prompt():
    prompt = """
    You are a QA Lead with 20 years of networking experience.

    Prepare a test plan for

    Firewall High Availability.

    Include

    Objectives

    Scope

    Risks

    Test Cases

    Exit Criteria
    """

    print(ask_llm(prompt))

def self_consisitency_prompt():
    prompt = """
    You are a Senior Network QA Engineer.

    A customer reports:

    • High latency
    • Packet loss
    • Slow application response

    Generate THREE independent reasoning paths.

    For each reasoning path:

    1. Identify the probable root cause.
    2. Explain your reasoning.
    3. Suggest troubleshooting steps.

    Finally,

    Compare the three reasoning paths.

    Return the MOST CONSISTENT root cause with justification.
    """

    print(ask_llm(prompt))


def least_to_most_prompt():
    prompt = """
    You are a Senior Network QA Engineer.

    A customer reports:

    • Cannot access websites
    • Cannot ping external IPs
    • VPN connection fails

    Solve the problem using Least-to-Most Prompting.

    Start from the simplest verification and gradually move to advanced troubleshooting.

    Step 1:
    Verify physical connectivity.

    Step 2:
    Verify IP configuration.

    Step 3:
    Verify subnet mask.

    Step 4:
    Verify default gateway.

    Step 5:
    Verify DNS.

    Step 6:
    Verify routing.

    Step 7:
    Verify firewall.

    Step 8:
    Verify VPN.

    For every step:

    • Explain what you checked.
    • Mention the expected result.
    • Mention whether the issue is found.

    Finally identify the root cause.
    """

    print(ask_llm(prompt))

def meta_prompt():
    prompt = """
    You are an Expert Prompt Engineer.

    Create an optimized prompt that will instruct an AI model to generate detailed OSPF test cases for Network QA Engineers.

    The generated prompt should include:

    1. Functional test cases
    2. Negative test cases
    3. Boundary test cases
    4. Expected results
    5. Test priority
    6. Output as a Markdown table

    Do not generate the test cases.

    Only generate the prompt.
    """

    print(ask_llm(prompt))

def prompt_chaining():
    prompt1 = """
    You are a Senior Network QA Engineer.

    Identify all possible reasons why OSPF neighbors are not forming.

    Return only the list.
    """

    output1 = ask_llm(prompt1)

    print(output1)

    prompt2 = f"""
    You are a Senior Network QA Engineer.

    Using the following possible causes:

    {output1}

    Generate troubleshooting steps for each issue.
    """

    output2 = ask_llm(prompt2)

    print(output2)

    prompt3 = f"""
    You are a Senior Network QA Engineer.

    Using these troubleshooting steps:

    {output2}

    Generate comprehensive QA test cases.

    Return the output as a Markdown table.
    """

    output3 = ask_llm(prompt3)

    print(output3)

def template_prompting():
    network_issue = "Users cannot access HTTPS websites"

    device = "Cisco ISR 4331"

    prompt = f"""
    You are a Senior Network Engineer.

    Analyze the following network issue.

    Device:
    {"CISCO NCS1K"}

    Issue:
    {"device not connected"}

    Provide:

    1. Root Cause
    2. Reason
    3. Troubleshooting Steps
    4. Recommendation
    """

    print(ask_llm(prompt))

    prompt = """
    You are a Senior Network Engineer.

    A company reports that users cannot access the internet.

    Use Question Decomposition Prompting.

    Break the problem into the following questions and answer each one.

    Question 1:
    Is the physical network connection working?

    Question 2:
    Are the router interfaces up?

    Question 3:
    Are users receiving valid IP addresses?

    Question 4:
    Is the default gateway reachable?

    Question 5:
    Is DNS working correctly?

    Question 6:
    Are firewall or ACL rules blocking traffic?

    Finally,

    Provide the most likely root cause and recommend a solution.
    """

    print(ask_llm(prompt))

def delimiter_prompting():

    prompt = """
    You are a Senior Network Engineer.

    Instructions:
    '''
    Analyze the network issue.
    '''

    Context:
    '''
    Router: Cisco ISR 4331
    Switch: Cisco Catalyst 9300
    VLAN 10 users cannot access HTTPS.
    '''

    Task:
    '''
    Provide:
    1. Root Cause
    2. Troubleshooting
    3. Recommendation
    '''
    """

    print(ask_llm(prompt))

def question_decomposition():
    prompt = """
    You are a Senior Network Engineer.

    A company reports that users cannot access the internet.

    Use Question Decomposition Prompting.

    Break the problem into the following questions and answer each one.

    Question 1:
    Is the physical network connection working?

    Question 2:
    Are the router interfaces up?

    Question 3:
    Are users receiving valid IP addresses?

    Question 4:
    Is the default gateway reachable?

    Question 5:
    Is DNS working correctly?

    Question 6:
    Are firewall or ACL rules blocking traffic?

    Finally,

    Provide the most likely root cause and recommend a solution.
    """

    print(ask_llm(prompt))


def iterative_prompting():
    prompt = """
    You are a Senior Network Engineer.

    A company reports that users cannot access HTTPS websites.

    Iteration 1:
    Identify the possible root cause.

    Iteration 2:
    Improve the previous answer by adding troubleshooting steps.

    Iteration 3:
    Improve the response again by recommending preventive measures.

    Return the final improved response.
    """

    print(ask_llm(prompt))

def reflection_prompting():
    prompt = """
    You are a Senior Network Engineer.

    Users cannot access HTTPS websites.

    Step 1:
    Provide an initial diagnosis.

    Step 2:
    Review your diagnosis and identify any missing information.

    Step 3:
    Improve the diagnosis.

    Step 4:
    Provide the final recommendation.
    """

    print(ask_llm(prompt))


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

    
def multimodal_prompting():

    image_data = encode_image("network_topology.png")

    response = client.chat.completions.create(

        model="gpt-4.1",

        messages=[
            {
                "role":"user",
                "content":[
                    {
                        "type":"text",
                        "text":"Analyze this network topology. Identify the root cause of the connectivity issue and recommend a solution."
                    },
                    {
                        "type":"image_url",
                        "image_url":{
                            "url":f"data:image/png;base64,{image_data}"
                        }
                    }
                ]
            }
        ]
    )

    print(response.choices[0].message.content)


def constitutional_prompt():
    prompt = """
    You are a Senior Network Engineer.

    Follow these principles while answering:

    1. Never assume missing information.
    2. Explain your reasoning clearly.
    3. Recommend only industry best practices.
    4. Mention uncertainties when appropriate.
    5. Do not suggest actions that could disrupt production without verification.

    Problem:

    Users cannot access HTTPS websites.

    Analyze the issue and recommend a solution.
    """

    print(ask_llm(prompt))

def agentic_prompt():
    prompt = """
    You are an AI Network Operations Agent.

    Your goal is to restore internet connectivity for users in VLAN 10.

    Network Details

    Router : Cisco ISR 4331
    Switch : Cisco Catalyst 9300

    Problem:
    Users in VLAN 10 cannot access HTTPS websites.
    Users in VLAN 20 can access the internet.

    Act as an intelligent AI Agent.

    Perform the following tasks.

    Step 1 - Planning
    Create a troubleshooting plan.

    Step 2 - Decision Making
    Determine which network components should be checked first and explain why.

    Step 3 - Task Execution
    Analyze:
    - Physical connectivity
    - VLAN configuration
    - Router interfaces
    - Default gateway
    - DNS
    - Firewall
    - ACL

    Step 4 - Root Cause Analysis
    Identify the most likely root cause.

    Step 5 - Solution
    Recommend corrective actions.

    Step 6 - Verification
    Describe how you would verify that the issue has been resolved.

    Step 7 - Final Report
    Generate a summary report including:
    - Issue
    - Root Cause
    - Actions Taken
    - Final Recommendation
    """

    print(ask_llm(prompt))


zeroshot()
one_shot()
few_shot()
role_prompt()
Instruction_prompt()
contextual_prompt()
chain_of_thoughts()
tree_of_thoughts()
persona_prompt()
self_consisitency_prompt()
least_to_most_prompt()
meta_prompt()
prompt_chaining()
template_prompting()
delimiter_prompting()
question_decomposition()
iterative_prompting()
reflection_prompting()
multimodal_prompting()
constitutional_prompt()
agentic_prompt()














